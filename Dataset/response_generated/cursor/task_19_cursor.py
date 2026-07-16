from bisect import bisect_left
from typing import List, TypeVar

T = TypeVar("T", int, float)


def longest_increasing_subsequence(nums: List[T]) -> List[T]:
    """Return one longest strictly increasing subsequence."""
    if not nums:
        return []

    tails: List[T] = []
    tails_idx: List[int] = []
    prev = [-1] * len(nums)

    for i, x in enumerate(nums):
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[pos] = x
            tails_idx[pos] = i
        if pos > 0:
            prev[i] = tails_idx[pos - 1]

    result: List[T] = []
    k = tails_idx[-1]
    while k != -1:
        result.append(nums[k])
        k = prev[k]

    result.reverse()
    return result