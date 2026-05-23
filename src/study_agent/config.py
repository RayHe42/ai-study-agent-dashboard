import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATABASE_PATH = os.environ.get(
    "STUDY_AGENT_DATABASE_PATH",
    str(BASE_DIR / "study_agent.db"),
)
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
