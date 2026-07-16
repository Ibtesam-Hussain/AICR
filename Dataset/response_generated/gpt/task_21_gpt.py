# Task: Write a function that merges overlapping intervals given a list of (start, end) tuples.

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals by the start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]
        # Check for overlap
        if current[0] <= last_merged[1]:
            # Merge the intervals
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)

    return merged
