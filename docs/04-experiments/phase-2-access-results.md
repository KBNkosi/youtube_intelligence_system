# Phase 2 Access Verification

This document records the live personal-account access test for the single
configured video. The machine-readable result is written to the ignored file
`data/raw/phase-2-access-check.json`.

## Configuration

- Video ID: `SKPvAFXAOqU`
- Access mode: channel
- Start date: `2026-06-03`
- End date: `2026-08-23`
- Content Owner/CMS access: not tested

## Result

Run completed at `2026-08-23T06:35:54.753200+00:00` UTC.

- OAuth: `CONFIRMED`
- Authenticated channel: `UCU-oV7BpTkSJ-33OqlT0JxQ` (`Kenny`)
- Video access: `CONFIRMED`
- Video: `AI-Assisted Healthcare Appointment Booking Platform | Project Demo`
- Video channel: `UCENlPswT6T0e_8DIe5DbYPg` (`Kenny Nkosi`)
- Channel/video relationship: `CONFIRMED` by account owner; the authenticated
	`Kenny` account owns/manages the `Kenny Nkosi` channel
- Analytics request: completed without an API error
- `channel==MINE`: accepted
- Retention row count: `0`
- Script-only classification: `UNKNOWN`

## Additional Evidence

After the API run, YouTube Studio was checked for the same channel/video.
The audience report displayed: `Not enough viewer data to show this report`.
The video has approximately `8` views.

This independent Studio observation is consistent with the Analytics API
returning zero retention rows because the video has insufficient viewer data.
It makes low-traffic data thresholding the leading explanation, but does not
prove that retention data is unavailable for videos with sufficient traffic.

## Phase 2 Interpretation

- Authentication and basic API access: `CONFIRMED`
- Account/channel ownership context: `CONFIRMED`
- Retention access for this low-traffic video: `CONDITIONAL`
- General retention API feasibility: `UNKNOWN`

The current result should not be classified as a platform-wide access failure.
The strongest next test is the same query against a higher-traffic video owned
or managed by the same account. That test can distinguish low-traffic data
thresholding from a broader query, date-range, or Analytics access problem.

The authenticated channel and video channel IDs differ, but the account owner
has confirmed that this is expected: `Kenny` is the Google account under which
the `Kenny Nkosi` channel belongs. The current run proves authentication and
request execution. The Studio message and approximately eight views provide
supporting evidence for insufficient data on this specific video.

No alignment conclusion should be made from this phase alone.