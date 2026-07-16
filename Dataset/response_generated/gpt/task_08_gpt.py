from collections import Counter
from typing import Dict


def count_error_types(log_file_path: str) -> Dict[str, int]:
    """
    Parse a log file and count occurrences of each error type.

    Expected log format (example):
        2026-07-15 10:30:12 ERROR DatabaseError: Connection failed

    The error type is assumed to be the first token immediately following
    the word 'ERROR'.
    """
    counts = Counter()

    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "ERROR" not in line:
                continue

            parts = line.split()
            try:
                error_index = parts.index("ERROR") + 1
                if error_index < len(parts):
                    error_type = parts[error_index].rstrip(":")
                    counts[error_type] += 1
            except ValueError:
                continue

    return dict(counts)