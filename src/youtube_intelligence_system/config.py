from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

VIDEO_ID = "SKPvAFXAOqU"
START_DATE = "2026-06-03"
END_DATE = "2026-08-23"

CLIENT_SECRET_PATH = SRC_DIR / "client_secret.json"
TOKEN_PATH = PROJECT_ROOT / "runtime" / "oauth" / "token.json"
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
PHASE_2_RESULT_PATH = RAW_DATA_DIR / "phase-2-access-check.json"


def ensure_runtime_directories() -> None:
    for directory in (TOKEN_PATH.parent, RAW_DATA_DIR, PROCESSED_DATA_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def validate_configuration() -> None:
    if not VIDEO_ID:
        raise ValueError("VIDEO_ID must be configured")
    if START_DATE > END_DATE:
        raise ValueError("START_DATE must not be later than END_DATE")
    if not CLIENT_SECRET_PATH.is_file():
        raise FileNotFoundError(
            f"OAuth client secret file was not found: {CLIENT_SECRET_PATH}"
        )