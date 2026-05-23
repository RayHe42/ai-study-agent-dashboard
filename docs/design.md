# Design Document

## Goal

A local single-user web app for studying. Users write notes, then ask AI to summarize or generate study tasks.

## Data Model

**notes table (SQLite)**

| Column | Type | Constraint |
|--------|------|------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| title | TEXT | NOT NULL |
| content | TEXT | NOT NULL |
| summary | TEXT | nullable (filled by AI later) |
| tasks | TEXT | nullable (filled by AI later) |
| created_at | TEXT | NOT NULL, ISO 8601 timestamp |
| updated_at | TEXT | NOT NULL, ISO 8601 timestamp |

## API Routes

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check, returns `{"status": "ok"}` |
| GET | / | Home page with note list |
| GET | /api/notes/ | List all notes |
| POST | /api/notes/ | Create a note (body: title, content) |
| GET | /api/notes/{id} | Get a single note |
| PUT | /api/notes/{id} | Update a note (body: title, content) |
| DELETE | /api/notes/{id} | Delete a note |

## Storage

SQLite via Python standard library `sqlite3`. Single file `study_agent.db` created at startup.

**Architecture:**
- `config.py` — `DATABASE_PATH` (configurable via `STUDY_AGENT_DATABASE_PATH` env var)
- `database.py` — `get_connection()` and `init_db()` (creates the notes table)
- `repository.py` — SQL queries: `insert_note`, `select_all_notes`, `select_note_by_id`, `update_note`, `delete_note`
- `routes/notes.py` — HTTP layer, uses FastAPI `Depends` to inject DB connection

## AI Design

All AI calls go through `ai_client.py`. Current mode: mock (returns fixed text). Future: swap in a real API client without changing route code.

## Scope Exclusions

- No user auth
- No real AI API
- No .env or secrets
- No React / SPA frontend
- No RAG or PDF parsing
