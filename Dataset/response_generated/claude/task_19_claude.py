from bisect import bisect_left
from typing import List

def longest_increasing_subsequence(nums: List[int]) -> List[int]:
    if not nums:
        return []

    n = len(nums)
    tails_idx = []          # indices of smallest tail of each length
    prev = [-1] * n         # predecessor indices for reconstruction

    for i, x in enumerate(nums):
        pos = bisect_left([nums[j] for j in tails_idx], x)
        if pos == len(tails_idx):
            tails_idx.append(i)
        else:
            tails_idx[pos] = i
        if pos > 0:
            prev[i] = tails_idx[pos - 1]

    # Reconstruct sequence
    result = []
    k = tails_idx[-1]
    while k != -1:
        result.append(nums[k])
        k = prev[k]

    return result[::-1]