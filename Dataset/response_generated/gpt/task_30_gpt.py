# Task: Write a function that compares two version strings (like "1.2.3" vs "1.10.0") to see which is newer.

def compare_versions(version1: str, version2: str) -> int:
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    # Compare parts of the version
    for v1, v2 in zip(v1_parts, v2_parts):
        if v1 != v2:
            return (v1 > v2) - (v1 < v2)
    
    # Handle cases where versions have a different number of parts
    return (len(v1_parts) > len(v2_parts)) - (len(v1_parts) < len(v2_parts))
