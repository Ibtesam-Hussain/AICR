def compare_versions(v1: str, v2: str) -> int:
    """Return 1 if v1 is newer, -1 if v2 is newer, 0 if equal."""
    parts1 = [int(part) for part in v1.split(".")]
    parts2 = [int(part) for part in v2.split(".")]

    max_len = max(len(parts1), len(parts2))
    parts1.extend([0] * (max_len - len(parts1)))
    parts2.extend([0] * (max_len - len(parts2)))

    for left, right in zip(parts1, parts2):
        if left > right:
            return 1
        if left < right:
            return -1
    return 0
