def second_largest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    
    if second == float('-inf'):
        raise ValueError("No second largest element (duplicates or insufficient distinct values)")
    
    return second