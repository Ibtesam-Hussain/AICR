import re

_EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

def extract_emails(text: str) -> list[str]:
    """Return all email addresses found in the given text."""
    return _EMAIL_PATTERN.findall(text)