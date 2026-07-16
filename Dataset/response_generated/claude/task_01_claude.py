import csv
from io import StringIO

def parse_csv(csv_string: str) -> list[dict]:
    """Parse a CSV string and return a list of dictionaries, one per row."""
    reader = csv.DictReader(StringIO(csv_string))
    return [dict(row) for row in reader]