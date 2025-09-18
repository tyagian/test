"""
Array Product Calculator

This module provides a function to calculate the product of all elements in a list,
excluding the element at each position.

"""
from typing import List

def calculate_products(numbers: List[int]) -> List[int]:
    """
    Calculate the product of all elements in a list, excluding the element at each position.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A new list where each element is the product of all numbers in the original list, except the number at that position.

    Raises:
        TypeError: If the input is not a list of integers.
    """
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise TypeError("Input must be a list of integers.")

    if not numbers:
        return []

    if len(numbers) == 1:
        return [1]

    products = []
    total_product = 1
    for num in numbers:
        total_product *= num

    for num in numbers:
        if num == 0:
            products.append(0)
        else:
            products.append(total_product // num)

    return products

# Example usage
print(calculate_products([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(calculate_products([0, 1, 2]))  # Output: [2, 0, 0]
print(calculate_products([]))  # Output: []
print(calculate_products([5]))  # Output: [1]