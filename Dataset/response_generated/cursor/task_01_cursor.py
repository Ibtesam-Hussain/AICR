import csv
from io import StringIO


def parse_csv(csv_string: str) -> list[dict[str, str]]:
    """Parse a CSV string into a list of row dictionaries (header row as keys)."""
    if not csv_string or not csv_string.strip():
        return []

    reader = csv.DictReader(StringIO(csv_string.strip()))
    return [dict(row) for row in reader]