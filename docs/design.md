# Design Document

## Goal

A local single-user web app for studying. Users write notes, then ask AI to summarize or generate study tasks.

## Data Model

**Note**
- id: integer, primary key
- title: string
- content: text
- summary: text (nullable, filled by AI)
- tasks: text (nullable, filled by AI)
- created_at: datetime

## API Routes

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check, returns `{"status": "ok"}` |
| GET | / | Home page with note list |
| GET | /api/notes/ | List all notes (JSON) |
| POST | /api/notes/ | Create a note (JSON body: title, content) |
| GET | /api/notes/{id} | Get a single note by ID |
| POST | /api/notes/{id}/summarize | Generate summary |
| POST | /api/notes/{id}/tasks | Generate tasks |

## Storage

**Current stage (Lesson 29):** In-memory Python list. Notes are lost when the server restarts.

**Future:** SQLite via SQLAlchemy. Single file `study.db` created at startup.

## AI Design

All AI calls go through `ai_client.py`. Current mode: mock (returns fixed text). Future: swap in a real API client without changing route code.

## Scope Exclusions

- No user auth
- No real AI API
- No .env or secrets
- No React / SPA frontend
- No RAG or PDF parsing
