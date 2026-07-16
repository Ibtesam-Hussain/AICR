def second_largest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")

    largest = second = float("-inf")

    for n in numbers:
        if n > largest:
            second, largest = largest, n
        elif largest > n > second:
            second = n

    if second == float("-inf"):
        raise ValueError("No second largest number exists")

    return second