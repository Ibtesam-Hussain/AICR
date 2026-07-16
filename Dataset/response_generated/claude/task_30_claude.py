# Task: Write a function that compares two version strings (like "1.2.3" vs "1.10.0") to see which is newer.

from packaging import version

def compare_versions(ver1: str, ver2: str) -> int:
    """
    Compare two version strings.
    
    Args:
        ver1: First version string (e.g., "1.2.3")
        ver2: Second version string (e.g., "1.10.0")
    
    Returns:
        -1 if ver1 < ver2
         0 if ver1 == ver2
         1 if ver1 > ver2
    """
    v1 = version.parse(ver1)
    v2 = version.parse(ver2)
    
    if v1 < v2:
        return -1
    elif v1 > v2:
        return 1
    else:
        return 0

from functools import cmp_to_key

def compare_versions(ver1: str, ver2: str) -> int:
    """
    Compare two version strings.
    
    Args:
        ver1: First version string (e.g., "1.2.3")
        ver2: Second version string (e.g., "1.10.0")
    
    Returns:
        -1 if ver1 < ver2
         0 if ver1 == ver2
         1 if ver1 > ver2
    """
    def normalize(v: str) -> tuple:
        return tuple(map(int, v.split(".")))
    
    v1 = normalize(ver1)
    v2 = normalize(ver2)
    
    if v1 < v2:
        return -1
    elif v1 > v2:
        return 1
    else:
        return 0
