# Task: Write a recursive function to calculate the nth Fibonacci number.

def fibonacci(n):
    if n < 0:
        raise ValueError("Input cannot be a negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
