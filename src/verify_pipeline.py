import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from youtube_intelligence_system.config import (
    CLIENT_SECRET_PATH,
    END_DATE,
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

def run_test():
    validate_configuration()
    ensure_runtime_directories()
    print("Initiating Secure Authorization Flow...")
    data_api, analytics_api = get_authenticated_service()

    # ------ 1. EXTRACT DATA API METRICS & DURATION -----
    print("Query public Data API for duration metrics...")
    video_response = data_api.videos().list(part="contentDetails", id=VIDEO_ID).execute()

    # Check if the video exists and if the user has permission to access it
    if not video_response["items"]:
        print(f"No video found with ID: {VIDEO_ID} or you lack permission")
        return

    # Extract the ISO 8601 duration and convert it to total seconds
    iso_duration = video_response["items"][0]["contentDetails"]["duration"]
    total_seconds = int(pd.to_timedelta(iso_duration).total_seconds())
    print(f"Video Length Confirmed: {total_seconds} seconds")


    # ------ 2. EXTRACT TRANSCRIPT TIMESTAMPS -----
    print("Pulling timestamp content transcript data...")
    try:
        transcript_api = YouTubeTranscriptApi()
        transcript = transcript_api.fetch(VIDEO_ID)
        raw_transcript = transcript.to_raw_data()
        df_transcript = pd.DataFrame(raw_transcript)
        df_transcript["end"] = df_transcript["start"] + df_transcript["duration"]
        print(f"Extracted {len(df_transcript)} text segments successfully.")
    except Exception as e:
        print(f"Transcript failure (Ensure captions are enabled): {e}")
        return


    # ----- 3. EXTRACT PRIVATE RETENTION TIMELINE -----
    print("Querying Analytics API for audience retention time-series data...")
    analytics_response = analytics_api.reports().query(
        ids="channel==MINE",
        startDate=START_DATE,
        endDate=END_DATE,
        metrics="audienceWatchRatio",
        dimensions="elapsedVideoTimeRatio",
        filters=f"video=={VIDEO_ID}",
    ).execute()

    retention_rows = analytics_response.get("rows", [])
    if not retention_rows:
        print("Error: No retention data found for the specified video.")
        return

    df_retention = pd.DataFrame(retention_rows, columns=["ratio", "retention_pct"])
    print(f"Extracted {len(df_retention)} normalized performance data intervals.")

    # ----- 4. RE-SCALING ALIGNMENT -----
    print("Mapping transcript timestamps to retention data intervals...")
    df_retention["calculated_seconds"] = df_retention["ratio"] * total_seconds

    def locate_transcript_text(sec):
        """
        Locate the transcript text corresponding to a given second.
        """
        match = df_transcript[(df_transcript["start"] <= sec) & (df_transcript["end"] >= sec)]
        return match["text"].values if not match.empty else "[No Transcript Available]"

    df_retention["aligned_content"] = df_retention["calculated_seconds"].apply(locate_transcript_text)

    # ----- 5. OUTPUT RESULTS -----
    print("\n --- Final Output ---")
    for index, row in df_retention.iloc[::10].iterrows():  # Displaying only the first 10 rows for brevity
        print(f"Time: {row['calculated_seconds']:>6.1f}s | Retention: {row['retention_pct']*100:>5.1f}% | Script: \"{row['aligned_content']}\"")


if __name__ == "__main__":
    run_test()