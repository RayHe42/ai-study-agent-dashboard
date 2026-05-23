import sqlite3
from datetime import datetime, timezone


def _row_to_dict(row: sqlite3.Row) -> dict:
    return dict(row)


def insert_note(conn: sqlite3.Connection, title: str, content: str) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    cursor = conn.execute(
        "INSERT INTO notes (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)",
        (title, content, now, now),
    )
    conn.commit()
    return {
        "id": cursor.lastrowid,
        "title": title,
        "content": content,
        "summary": None,
        "tasks": None,
        "created_at": now,
        "updated_at": now,
    }


def select_all_notes(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute("SELECT * FROM notes ORDER BY id").fetchall()
    return [_row_to_dict(r) for r in rows]


def select_note_by_id(conn: sqlite3.Connection, note_id: int) -> dict | None:
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    if row is None:
        return None
    return _row_to_dict(row)


def update_note(
    conn: sqlite3.Connection, note_id: int, title: str, content: str
) -> dict | None:
    now = datetime.now(timezone.utc).isoformat()
    cursor = conn.execute(
        "UPDATE notes SET title = ?, content = ?, updated_at = ? WHERE id = ?",
        (title, content, now, note_id),
    )
    conn.commit()
    if cursor.rowcount == 0:
        return None
    return select_note_by_id(conn, note_id)


def delete_note(conn: sqlite3.Connection, note_id: int) -> bool:
    cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    return cursor.rowcount > 0
