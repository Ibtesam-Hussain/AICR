import re
from collections import Counter

def count_error_types(file_path, pattern=r'\b([A-Z][a-zA-Z]*(?:Error|Exception))\b'):
    """
    Parse a log file and count occurrences of each error type.

    Args:
        file_path (str): Path to the log file.
        pattern (str): Regex pattern to identify error types.
                        Defaults to matching words ending in 'Error' or 'Exception'.

    Returns:
        Counter: A Counter mapping error type -> count.
    """
    error_counts = Counter()
    regex = re.compile(pattern)

    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                matches = regex.findall(line)
                error_counts.update(matches)
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading log file {file_path}: {e}")

    return error_counts