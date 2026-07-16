from bisect import bisect_left


def longest_increasing_subsequence(nums):
    """
    Return the longest strictly increasing subsequence as a list.
    Runs in O(n log n) time.
    """
    if not nums:
        return []

    tails = []
    tails_idx = []
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

    result = []
    idx = tails_idx[-1]
    while idx != -1:
        result.append(nums[idx])
        idx = prev[idx]

    return result[::-1]