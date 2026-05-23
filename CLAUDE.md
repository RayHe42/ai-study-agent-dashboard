# CLAUDE.md — AI Study Agent Dashboard

## What This Is

A local single-user AI study assistant built with FastAPI. Users add notes and get AI-generated summaries and tasks.

## Tech Stack

- Python 3.11+ / FastAPI / Jinja2 / SQLite / SQLAlchemy / Pydantic
- pytest for testing

## How To Run

```bash
pip install -r requirements.txt
pip install -e .
uvicorn study_agent.main:app --reload
```

## How To Test

```bash
pytest tests/ -v
```

## Rules

- No .env files. No API keys. No secrets in code.
- No login/registration system.
- AI features use mock responses only — never call real APIs.
- No React or other frontend frameworks. Jinja2 templates only.
- Write tests for new logic. Keep tests simple and focused.
- This project is for beginners. Code should be readable and straightforward.
- Do not add complexity beyond what is asked.
