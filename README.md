# AI Study Agent Dashboard

Local single-user AI study assistant web app. Add notes, view them, and generate AI-powered summaries and study tasks.

## Quick Start

```bash
pip install -r requirements.txt
pip install -e .
uvicorn study_agent.main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## Run Tests

```bash
pytest tests/ -v
```

## Project Structure

```
src/study_agent/
  main.py          — FastAPI app entry point
  config.py        — app settings
  database.py      — SQLite init and helpers
  models.py        — SQLAlchemy ORM models
  schemas.py       — Pydantic request/response schemas
  prompts.py       — prompt builders for AI tasks
  ai_client.py     — AI client (mock mode)
  routes/
    notes.py       — REST API for notes
    web.py         — HTML page routes
  templates/       — Jinja2 HTML templates
tests/
  test_prompts.py  — prompt builder tests
  test_database.py — database init tests
```

## Current Status

Lesson 29: project skeleton only. AI features use mock responses.
