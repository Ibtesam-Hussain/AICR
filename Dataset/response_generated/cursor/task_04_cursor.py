import re

_EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    re.IGNORECASE,
)

def extract_emails(text: str) -> list[str]:
    """Return unique email addresses found in text, in order of appearance."""
    if not text:
        return []
    return list(dict.fromkeys(_EMAIL_RE.findall(text)))