from typing import Iterable


def second_largest(numbers: Iterable[int | float]) -> int | float:
    unique = set(numbers)
    if len(unique) < 2:
        raise ValueError("At least two distinct numbers are required.")

    largest = second = float("-inf")
    for num in unique:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second