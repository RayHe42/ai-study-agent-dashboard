def build_summary_prompt(content: str) -> str:
    """Build a prompt that asks the AI to summarize study notes."""
    return (
        "You are a study assistant. "
        "Summarize the following study note in 2-3 sentences.\n\n"
        f"Note:\n{content}"
    )


def build_tasks_prompt(content: str) -> str:
    """Build a prompt that asks the AI to generate study tasks from notes."""
    return (
        "You are a study assistant. "
        "Based on the following study note, generate 3 actionable study tasks. "
        "Return each task on a new line, starting with a dash.\n\n"
        f"Note:\n{content}"
    )
