from datetime import datetime


def sort_dates(date_strings: list[str], *, fmt: str = "%Y-%m-%d") -> list[str]:
    """Return date strings sorted chronologically (earliest first)."""
    return sorted(date_strings, key=lambda s: datetime.strptime(s, fmt))