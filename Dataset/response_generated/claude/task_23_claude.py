# Task: Write a function that returns the top K most frequent elements in a list.

from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def top_k_frequent(elements: List[T], k: int) -> List[T]:
    """
    Returns the top K most frequent elements in a list.
    
    Args:
        elements: List of elements to analyze
        k: Number of top frequent elements to return
        
    Returns:
        List of top K most frequent elements ordered by frequency (descending)
        
    Raises:
        ValueError: If k is negative or greater than number of unique elements
    """
    if k < 0:
        raise ValueError("k must be non-negative")
    
    if k == 0:
        return []
    
    counter = Counter(elements)
    
    if k > len(counter):
        raise ValueError(f"k ({k}) cannot be greater than number of unique elements ({len(counter)})")
    
    return [element for element, _ in counter.most_common(k)]
