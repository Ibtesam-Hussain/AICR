from collections import Counter

def are_anagrams(s1: str, s2: str) -> bool:
    """
    Return True if s1 and s2 are anagrams of each other, otherwise False.
    Whitespace is ignored and comparison is case-insensitive.
    """
    normalized1 = "".join(s1.lower().split())
    normalized2 = "".join(s2.lower().split())

    return Counter(normalized1) == Counter(normalized2)