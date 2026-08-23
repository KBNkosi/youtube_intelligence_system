## YouTube Intelligence System

This repository contains a single-video experiment for testing whether
YouTube audience-retention samples can be associated with timestamped
transcript segments.

### Phase 1 setup

Requirements:

- Python 3.13
- `uv`
- A Google OAuth desktop client secret saved as `src/client_secret.json`

Install the locked dependencies and development tools:

```text
uv sync --dev
```

The experiment is limited to the configured video and date range in
`src/youtube_intelligence_system/config.py`.

Run the verification script from the repository root with:

```text
uv run python src/verify_pipeline.py
```

The script resolves the credential path from the project location, so the
current working directory does not determine where credentials are found.
The first run opens the read-only OAuth flow. The resulting token is stored
under `runtime/oauth/` and reused or refreshed on later runs.

Local raw evidence belongs in `data/raw/`; generated outputs belong in
`data/processed/`. These locations, the OAuth token, and client credentials
are ignored by Git and must not be committed.
