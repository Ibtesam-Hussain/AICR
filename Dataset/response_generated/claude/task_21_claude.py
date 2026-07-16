# Task: Write a function that merges overlapping intervals given a list of (start, end) tuples.

def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []
    
    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]
    
    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return merged

print(merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]))
# Output: [(1, 6), (8, 10), (15, 18)]

print(merge_intervals([(1, 4), (4, 5)]))
# Output: [(1, 5)]

print(merge_intervals([]))
# Output: []
