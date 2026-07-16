import csv
import io


def parse_csv(csv_string: str) -> list[dict[str, str]]:
    """
    Parse a CSV string into a list of dictionaries, one per row.
    """
    if not csv_string.strip():
        return []

    reader = csv.DictReader(io.StringIO(csv_string))
    return [dict(row) for row in reader]