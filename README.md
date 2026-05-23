# AI Study Agent Dashboard

Local single-user AI study assistant web app. Add notes, view them, and generate AI-powered summaries and study tasks.

## Quick Start

```bash
pip install -r requirements.txt
pip install -e .
uvicorn study_agent.main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

Notes are saved to `study_agent.db` (SQLite). Data persists across server restarts.

## Run Tests

```bash
pytest tests/ -v
```

## Try the API

```bash
# Health check
curl http://127.0.0.1:8000/health

# List notes (empty at first)
curl http://127.0.0.1:8000/api/notes/

# Create a note
curl -X POST http://127.0.0.1:8000/api/notes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Basics", "content": "Variables, loops, functions"}'

# Get a note by ID
curl http://127.0.0.1:8000/api/notes/1

# Update a note
curl -X PUT http://127.0.0.1:8000/api/notes/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Basics v2", "content": "Updated content"}'

# Delete a note
curl -X DELETE http://127.0.0.1:8000/api/notes/1
```

## Project Structure

```
src/study_agent/
  main.py          — FastAPI app entry point
  config.py        — app settings (database path, template dir)
  database.py      — SQLite connection and table init
  repository.py    — SQL queries (CRUD for notes)
  models.py        — placeholder (no ORM)
  schemas.py       — Pydantic request/response schemas
  prompts.py       — prompt builders for AI tasks
  ai_client.py     — AI client (mock mode)
  routes/
    notes.py       — REST API for notes
    web.py         — HTML page routes
  templates/       — Jinja2 HTML templates
tests/
  test_database.py — database init tests
  test_repository.py — repository CRUD tests
  test_routes.py   — API route tests
  test_prompts.py  — prompt builder tests
```

## Current Status

Lesson 30: notes API with SQLite persistence. AI features use mock responses.
