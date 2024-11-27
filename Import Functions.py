import math
import random

# Function 1: Square root with exception
def square_root(number):
    """
    Returns the square root of a number.
    Raises:
        ValueError: If the input is negative.
    """
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(number)

# Function 2: Random integer processing
def process_random_integer():
    """
    Generates a random integer between 1 and 100.
    Processes the number as follows:
        - If odd, multiplies by 2.
        - If divisible by 3, divides by 3.
        - If divisible by 4, multiplies by 4.
        - If greater than 4 after processing, raises an exception.
    Returns:
        The processed number if valid.
    Raises:
        ValueError: If the number is greater than 4.
    """
    num = random.randint(1, 100)
    if num % 2 != 0:  # Odd
        num *= 2
    if num % 3 == 0:  # Divisible by 3
        num //= 3
    if num % 4 == 0:  # Divisible by 4
        num *= 4
    if num > 4:
        raise ValueError(f"Number exceeds 4: {num}")
    return num

# Function 3: List of divisibles
def list_divisibles(n):
    """
    Returns a list of integers between 1 and 10 (inclusive) divisible by the given number.
    Args:
        n (int): The divisor.
    Returns:
        list: Numbers divisible by `n`.
    """
    return [i for i in range(1, 11) if i % n == 0]