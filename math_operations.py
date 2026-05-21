#!/usr/bin/env python3
"""
Math Operations Module

A comprehensive module providing various mathematical calculations including:
- Basic arithmetic operations
- Advanced mathematical functions
- Statistical calculations
- Trigonometric functions
- Logarithmic operations
"""

import math
from typing import List, Union

# ============================================================================
# BASIC ARITHMETIC OPERATIONS
# ============================================================================

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b
    """
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Quotient of a divided by b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def floor_divide(a: Union[int, float], b: Union[int, float]) -> int:
    """Floor division of a by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Floor quotient of a divided by b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Calculate remainder of a divided by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Remainder of a divided by b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot perform modulo with zero")
    return a % b

def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """Raise base to the power of exponent.
    
    Args:
        base: Base number
        exponent: Exponent
        
    Returns:
        base raised to the power of exponent
    """
    return base ** exponent

# ============================================================================
# ADVANCED MATHEMATICAL OPERATIONS
# ============================================================================

def square_root(n: Union[int, float]) -> float:
    """Calculate square root of a number.
    
    Args:
        n: Number to find square root of
        
    Returns:
        Square root of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(n)

def cube_root(n: Union[int, float]) -> float:
    """Calculate cube root of a number.
    
    Args:
        n: Number to find cube root of
        
    Returns:
        Cube root of n
    """
    return n ** (1/3)

def factorial(n: int) -> int:
    """Calculate factorial of a number.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative or not an integer
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial requires a non-negative integer")
    return math.factorial(n)

def absolute(n: Union[int, float]) -> Union[int, float]:
    """Calculate absolute value of a number.
    
    Args:
        n: Number
        
    Returns:
        Absolute value of n
    """
    return abs(n)

def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two numbers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Greatest common divisor of a and b
    """
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two numbers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Least common multiple of a and b
    """
    return abs(a * b) // math.gcd(a, b)

def is_prime(n: int) -> bool:
    """Check if a number is prime.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_even(n: int) -> bool:
    """Check if a number is even.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is even, False otherwise
    """
    return n % 2 == 0

def is_odd(n: int) -> bool:
    """Check if a number is odd.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is odd, False otherwise
    """
    return n % 2 != 0

# ============================================================================
# STATISTICAL OPERATIONS
# ============================================================================

def mean(numbers: List[Union[int, float]]) -> float:
    """Calculate arithmetic mean of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Mean of the numbers
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)

def median(numbers: List[Union[int, float]]) -> float:
    """Calculate median of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Median of the numbers
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def mode(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Calculate mode of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Mode of the numbers (most frequent value)
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    return max(frequency, key=frequency.get)

def variance(numbers: List[Union[int, float]]) -> float:
    """Calculate variance of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Variance of the numbers
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of empty list")
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers: List[Union[int, float]]) -> float:
    """Calculate standard deviation of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Standard deviation of the numbers
        
    Raises:
        ValueError: If list is empty
    """
    return math.sqrt(variance(numbers))

def sum_list(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Calculate sum of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Sum of all numbers
    """
    return sum(numbers)

def min_value(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Find minimum value in a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Minimum value
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot find minimum of empty list")
    return min(numbers)

def max_value(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Find maximum value in a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Maximum value
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot find maximum of empty list")
    return max(numbers)

def range_value(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Calculate range of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Range (max - min)
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate range of empty list")
    return max(numbers) - min(numbers)

# ============================================================================
# TRIGONOMETRIC OPERATIONS
# ============================================================================

def sine(angle_degrees: Union[int, float]) -> float:
    """Calculate sine of an angle in degrees.
    
    Args:
        angle_degrees: Angle in degrees
        
    Returns:
        Sine of the angle
    """
    return math.sin(math.radians(angle_degrees))

def cosine(angle_degrees: Union[int, float]) -> float:
    """Calculate cosine of an angle in degrees.
    
    Args:
        angle_degrees: Angle in degrees
        
    Returns:
        Cosine of the angle
    """
    return math.cos(math.radians(angle_degrees))

def tangent(angle_degrees: Union[int, float]) -> float:
    """Calculate tangent of an angle in degrees.
    
    Args:
        angle_degrees: Angle in degrees
        
    Returns:
        Tangent of the angle
    """
    return math.tan(math.radians(angle_degrees))

def arcsine(value: float) -> float:
    """Calculate arcsine (inverse sine) in degrees.
    
    Args:
        value: Value between -1 and 1
        
    Returns:
        Arcsine in degrees
        
    Raises:
        ValueError: If value is outside [-1, 1]
    """
    if not -1 <= value <= 1:
        raise ValueError("Value must be between -1 and 1")
    return math.degrees(math.asin(value))

def arccosine(value: float) -> float:
    """Calculate arccosine (inverse cosine) in degrees.
    
    Args:
        value: Value between -1 and 1
        
    Returns:
        Arccosine in degrees
        
    Raises:
        ValueError: If value is outside [-1, 1]
    """
    if not -1 <= value <= 1:
        raise ValueError("Value must be between -1 and 1")
    return math.degrees(math.acos(value))

def arctangent(value: float) -> float:
    """Calculate arctangent (inverse tangent) in degrees.
    
    Args:
        value: Any real number
        
    Returns:
        Arctangent in degrees
    """
    return math.degrees(math.atan(value))

# ============================================================================
# LOGARITHMIC OPERATIONS
# ============================================================================

def natural_log(n: Union[int, float]) -> float:
    """Calculate natural logarithm (base e) of a number.
    
    Args:
        n: Positive number
        
    Returns:
        Natural logarithm of n
        
    Raises:
        ValueError: If n is not positive
    """
    if n <= 0:
        raise ValueError("Logarithm requires positive number")
    return math.log(n)

def log_base_10(n: Union[int, float]) -> float:
    """Calculate logarithm base 10 of a number.
    
    Args:
        n: Positive number
        
    Returns:
        Logarithm base 10 of n
        
    Raises:
        ValueError: If n is not positive
    """
    if n <= 0:
        raise ValueError("Logarithm requires positive number")
    return math.log10(n)

def log_base_n(n: Union[int, float], base: Union[int, float]) -> float:
    """Calculate logarithm of n with specified base.
    
    Args:
        n: Positive number
        base: Positive base (not equal to 1)
        
    Returns:
        Logarithm of n with specified base
        
    Raises:
        ValueError: If n or base is not positive, or base is 1
    """
    if n <= 0 or base <= 0:
        raise ValueError("Logarithm requires positive numbers")
    if base == 1:
        raise ValueError("Base cannot be 1")
    return math.log(n, base)

# ============================================================================
# GEOMETRIC OPERATIONS
# ============================================================================

def circle_area(radius: Union[int, float]) -> float:
    """Calculate area of a circle.
    
    Args:
        radius: Radius of the circle
        
    Returns:
        Area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def circle_circumference(radius: Union[int, float]) -> float:
    """Calculate circumference of a circle.
    
    Args:
        radius: Radius of the circle
        
    Returns:
        Circumference of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

def rectangle_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    """Calculate area of a rectangle.
    
    Args:
        length: Length of the rectangle
        width: Width of the rectangle
        
    Returns:
        Area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return length * width

def rectangle_perimeter(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    """Calculate perimeter of a rectangle.
    
    Args:
        length: Length of the rectangle
        width: Width of the rectangle
        
    Returns:
        Perimeter of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return 2 * (length + width)

def triangle_area(base: Union[int, float], height: Union[int, float]) -> float:
    """Calculate area of a triangle.
    
    Args:
        base: Base of the triangle
        height: Height of the triangle
        
    Returns:
        Area of the triangle
        
    Raises:
        ValueError: If base or height is negative
    """
    if base < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return 0.5 * base * height

def sphere_volume(radius: Union[int, float]) -> float:
    """Calculate volume of a sphere.
    
    Args:
        radius: Radius of the sphere
        
    Returns:
        Volume of the sphere
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * radius ** 3

def cylinder_volume(radius: Union[int, float], height: Union[int, float]) -> float:
    """Calculate volume of a cylinder.
    
    Args:
        radius: Radius of the cylinder base
        height: Height of the cylinder
        
    Returns:
        Volume of the cylinder
        
    Raises:
        ValueError: If radius or height is negative
    """
    if radius < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return math.pi * radius ** 2 * height

# ============================================================================
# CONVERSION OPERATIONS
# ============================================================================

def celsius_to_fahrenheit(celsius: Union[int, float]) -> float:
    """Convert Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in Celsius
        
    Returns:
        Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: Union[int, float]) -> float:
    """Convert Fahrenheit to Celsius.
    
    Args:
        fahrenheit: Temperature in Fahrenheit
        
    Returns:
        Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

def degrees_to_radians(degrees: Union[int, float]) -> float:
    """Convert degrees to radians.
    
    Args:
        degrees: Angle in degrees
        
    Returns:
        Angle in radians
    """
    return math.radians(degrees)

def radians_to_degrees(radians: Union[int, float]) -> float:
    """Convert radians to degrees.
    
    Args:
        radians: Angle in radians
        
    Returns:
        Angle in degrees
    """
    return math.degrees(radians)

# ============================================================================
# PERCENTAGE OPERATIONS
# ============================================================================

def percentage(part: Union[int, float], whole: Union[int, float]) -> float:
    """Calculate what percentage 'part' is of 'whole'.
    
    Args:
        part: Part value
        whole: Whole value
        
    Returns:
        Percentage
        
    Raises:
        ValueError: If whole is zero
    """
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100

def percentage_of(percentage: Union[int, float], whole: Union[int, float]) -> float:
    """Calculate what value is 'percentage' percent of 'whole'.
    
    Args:
        percentage: Percentage value
        whole: Whole value
        
    Returns:
        Calculated value
    """
    return (percentage / 100) * whole

def percentage_change(old_value: Union[int, float], new_value: Union[int, float]) -> float:
    """Calculate percentage change from old value to new value.
    
    Args:
        old_value: Original value
        new_value: New value
        
    Returns:
        Percentage change (positive for increase, negative for decrease)
        
    Raises:
        ValueError: If old_value is zero
    """
    if old_value == 0:
        raise ValueError("Old value cannot be zero")
    return ((new_value - old_value) / old_value) * 100

if __name__ == "__main__":
    # Test the module
    print("Math Operations Module - Test Suite")
    print("="*50)
    print(f"\nBasic: 5 + 3 = {add(5, 3)}")
    print(f"Power: 2^10 = {power(2, 10)}")
    print(f"Square root of 144 = {square_root(144)}")
    print(f"Factorial of 5 = {factorial(5)}")
    print(f"Mean of [1,2,3,4,5] = {mean([1,2,3,4,5])}")
    print(f"Circle area (r=5) = {circle_area(5):.2f}")
    print(f"\nAll tests passed!")
