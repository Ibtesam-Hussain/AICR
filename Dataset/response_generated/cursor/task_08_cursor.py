import re
from collections import Counter
from pathlib import Path

_ERROR_PATTERN = re.compile(
    r"\b(?:ERROR|FATAL|CRITICAL)\b"
    r"(?:\s*[\[\]:]\s*|\s+)"
    r"(?P<type>\w+(?:Error|Exception)?)",
    re.IGNORECASE,
)


def count_error_types(log_path: str | Path) -> dict[str, int]:
    """Parse a log file and return a count of each error type."""
    counts: Counter[str] = Counter()

    with Path(log_path).open(encoding="utf-8", errors="replace") as f:
        for line in f:
            match = _ERROR_PATTERN.search(line)
            if match:
                counts[match.group("type")] += 1

    return dict(counts)