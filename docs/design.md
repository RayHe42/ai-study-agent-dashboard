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
| GET | / | Home page with note list |
| GET | /notes/new | New note form |
| POST | /notes | Create a note |
| GET | /notes/{id} | Note detail page |
| POST | /notes/{id}/summarize | Generate summary |
| POST | /notes/{id}/tasks | Generate tasks |

## AI Design

All AI calls go through `ai_client.py`. Current mode: mock (returns fixed text). Future: swap in a real API client without changing route code.

## Storage

SQLite via SQLAlchemy. Single file `study.db` created at startup.

## Scope Exclusions

- No user auth
- No real AI API
- No .env or secrets
- No React / SPA frontend
- No RAG or PDF parsing
