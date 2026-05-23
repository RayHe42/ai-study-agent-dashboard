from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'study.db'}"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
