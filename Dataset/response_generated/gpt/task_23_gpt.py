# Task: Write a function that returns the top K most frequent elements in a list.

from collections import Counter
import heapq

def top_k_frequent(nums, k):
    if k == 0:
        return []
    counter = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, counter.items(), key=lambda x: x[1])]
