from datetime import datetime

def sort_dates(date_strings, date_format="%Y-%m-%d"):
    """
    Sort a list of date strings chronologically.

    Args:
        date_strings (list[str]): List of date strings.
        date_format (str): Format of the input date strings (default: "%Y-%m-%d").

    Returns:
        list[str]: Chronologically sorted date strings.
    """
    return sorted(date_strings, key=lambda d: datetime.strptime(d, date_format))