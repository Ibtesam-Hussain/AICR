from collections import Counter


def are_anagrams(s1: str, s2: str) -> bool:
    a, b = s1.lower(), s2.lower()
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)