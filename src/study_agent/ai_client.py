"""AI client — currently returns mock responses.

To connect a real API later, replace the functions below
while keeping the same signatures.
"""


def summarize(content: str) -> str:
    """Return a mock summary of the given note content."""
    return f"[Mock Summary] This note covers the topic briefly."


def generate_tasks(content: str) -> list[str]:
    """Return a mock list of study tasks."""
    return [
        "[Mock] Review the key concepts",
        "[Mock] Practice with examples",
        "[Mock] Write a summary in your own words",
    ]
