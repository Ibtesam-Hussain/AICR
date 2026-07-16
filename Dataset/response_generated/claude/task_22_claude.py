# Task: Write a recursive function to calculate the nth Fibonacci number.

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using memoization for efficiency.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    memo = {}
    
    def fib(num: int) -> int:
        if num in memo:
            return memo[num]
        if num <= 1:
            return num
        memo[num] = fib(num - 1) + fib(num - 2)
        return memo[num]
    
    return fib(n)

print(fibonacci(10))  # Output: 55
print(fibonacci(0))   # Output: 0
print(fibonacci(1))   # Output: 1
