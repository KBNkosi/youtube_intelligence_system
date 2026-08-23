import json
from datetime import datetime, timezone

import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from youtube_intelligence_system.config import (
    CLIENT_SECRET_PATH,
    END_DATE,
    PHASE_2_RESULT_PATH,
    START_DATE,
    TOKEN_PATH,
    VIDEO_ID,
    ensure_runtime_directories,
    validate_configuration,
)

# Define the scopes for the Google API (Readonly access)
# We will require read-only access to the YouTube Data and Analytics API.
SCOPES = [
  "https://www.googleapis.com/auth/youtube.readonly",
  "https://www.googleapis.com/auth/yt-analytics.readonly"
  ]

# Retrieve the YouTube API service
def get_authenticated_service():
    """
    Authenticate and return the YouTube API service.
    """
    ensure_runtime_directories()
    credentials = None
    if TOKEN_PATH.exists():
        credentials = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_SECRET_PATH), SCOPES
            )
            credentials = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(credentials.to_json(), encoding="utf-8")

    # Build the YouTube Data API and YouTube Analytics API services
    data_api = build("youtube", "v3", credentials=credentials)
    analytics_api = build("youtubeAnalytics", "v2", credentials=credentials)
    return data_api, analytics_api


def describe_api_error(error):
    """Return safe, structured information about a Google API failure."""
    details = {
        "error_type": type(error).__name__,
        "status_code": None,
        "reason": str(error),
    }
    if isinstance(error, HttpError):
        details["status_code"] = error.resp.status
    return details


def write_phase_2_result(result):
    PHASE_2_RESULT_PATH.write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )


def run_phase_2_access_check():
    validate_configuration()
    ensure_runtime_directories()
    result = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "video_id": VIDEO_ID,
        "start_date": START_DATE,
        "end_date": END_DATE,
        "access_mode": "channel",
        "oauth": {"status": "not_started"},
        "authenticated_channel": {"status": "not_checked"},
        "video": {"status": "not_checked"},
        "analytics": {"status": "not_checked", "channel_mine": "not_checked"},
        "classification": "UNKNOWN",
    }

    print("Initiating read-only OAuth authorization...")
    try:
        data_api, analytics_api = get_authenticated_service()
        result["oauth"] = {"status": "CONFIRMED", "scopes": SCOPES}
    except Exception as error:
        result["oauth"] = {"status": "UNAVAILABLE", "error": describe_api_error(error)}
        result["classification"] = "UNAVAILABLE"
        write_phase_2_result(result)
        print(f"OAuth failed; result saved to {PHASE_2_RESULT_PATH}")
        return

    print("Checking the authenticated channel...")
    try:
        channel_response = data_api.channels().list(part="id,snippet", mine=True).execute()
        channels = channel_response.get("items", [])
        if len(channels) != 1:
            result["authenticated_channel"] = {
                "status": "UNKNOWN",
                "count": len(channels),
            }
        else:
            channel = channels[0]
            result["authenticated_channel"] = {
                "status": "CONFIRMED",
                "id": channel.get("id"),
                "title": channel.get("snippet", {}).get("title"),
            }
    except Exception as error:
        result["authenticated_channel"] = {
            "status": "UNAVAILABLE",
            "error": describe_api_error(error),
        }

    print(f"Checking access to video {VIDEO_ID}...")
    try:
        video_response = data_api.videos().list(
            part="contentDetails,snippet", id=VIDEO_ID
        ).execute()
        videos = video_response.get("items", [])
        if len(videos) != 1:
            result["video"] = {"status": "UNAVAILABLE", "count": len(videos)}
        else:
            video = videos[0]
            result["video"] = {
                "status": "CONFIRMED",
                "id": video.get("id"),
                "title": video.get("snippet", {}).get("title"),
                "channel_id": video.get("snippet", {}).get("channelId"),
                "channel_title": video.get("snippet", {}).get("channelTitle"),
                "duration": video.get("contentDetails", {}).get("duration"),
            }
    except Exception as error:
        result["video"] = {"status": "UNAVAILABLE", "error": describe_api_error(error)}

    authenticated_id = result["authenticated_channel"].get("id")
    video_channel_id = result["video"].get("channel_id")
    result["channel_video_relationship"] = {
        "status": "CONFIRMED" if authenticated_id == video_channel_id else "CONDITIONAL",
        "authenticated_channel_id": authenticated_id,
        "video_channel_id": video_channel_id,
    }

    print("Querying Analytics retention data with channel==MINE...")
    try:
        analytics_response = analytics_api.reports().query(
            ids="channel==MINE",
            startDate=START_DATE,
            endDate=END_DATE,
            metrics="audienceWatchRatio",
            dimensions="elapsedVideoTimeRatio",
            filters=f"video=={VIDEO_ID}",
        ).execute()
        rows = analytics_response.get("rows", [])
        result["analytics"] = {
            "status": "CONFIRMED" if rows else "UNKNOWN",
            "channel_mine": "CONFIRMED",
            "row_count": len(rows),
        }
        result["classification"] = "CONFIRMED" if rows else "UNKNOWN"
    except Exception as error:
        result["analytics"] = {
            "status": "UNAVAILABLE",
            "channel_mine": "UNAVAILABLE",
            "error": describe_api_error(error),
        }
        result["classification"] = "UNAVAILABLE"

    write_phase_2_result(result)
    print(f"Phase 2 result saved to {PHASE_2_RESULT_PATH}")
    print(f"Access classification: {result['classification']}")


if __name__ == "__main__":
    run_phase_2_access_check()