#!/usr/bin/env python3
"""
Hello World Python Script

A simple Python script that prints a greeting message and demonstrates math operations.
"""

import math_operations

def main():
    """Main function that prints Hello World message and demonstrates math operations."""
    print("Hello World!")
    print("This is a Python script added to the octocat/hello-world repository.")
    print("\n" + "="*50)
    print("Math Operations Demo")
    print("="*50)
    
    # Basic arithmetic
    print("\n--- Basic Arithmetic ---")
    print(f"10 + 5 = {math_operations.add(10, 5)}")
    print(f"10 - 5 = {math_operations.subtract(10, 5)}")
    print(f"10 * 5 = {math_operations.multiply(10, 5)}")
    print(f"10 / 5 = {math_operations.divide(10, 5)}")
    print(f"10 // 3 = {math_operations.floor_divide(10, 3)}")
    print(f"10 % 3 = {math_operations.modulo(10, 3)}")
    print(f"2 ** 8 = {math_operations.power(2, 8)}")
    
    # Advanced operations
    print("\n--- Advanced Operations ---")
    print(f"Square root of 16 = {math_operations.square_root(16)}")
    print(f"Factorial of 5 = {math_operations.factorial(5)}")
    print(f"Absolute value of -42 = {math_operations.absolute(-42)}")
    print(f"GCD of 48 and 18 = {math_operations.gcd(48, 18)}")
    print(f"LCM of 12 and 15 = {math_operations.lcm(12, 15)}")
    
    # Statistical operations
    print("\n--- Statistical Operations ---")
    numbers = [10, 20, 30, 40, 50]
    print(f"Numbers: {numbers}")
    print(f"Mean: {math_operations.mean(numbers)}")
    print(f"Median: {math_operations.median(numbers)}")
    print(f"Mode: {math_operations.mode([1, 2, 2, 3, 4])}")
    print(f"Standard Deviation: {math_operations.standard_deviation(numbers):.2f}")
    print(f"Variance: {math_operations.variance(numbers):.2f}")
    
    # Trigonometric operations
    print("\n--- Trigonometric Operations ---")
    angle = 45
    print(f"Sin({angle}°) = {math_operations.sine(angle):.4f}")
    print(f"Cos({angle}°) = {math_operations.cosine(angle):.4f}")
    print(f"Tan({angle}°) = {math_operations.tangent(angle):.4f}")
    
    # Logarithmic operations
    print("\n--- Logarithmic Operations ---")
    print(f"Natural log of 10 = {math_operations.natural_log(10):.4f}")
    print(f"Log base 10 of 100 = {math_operations.log_base_10(100):.4f}")
    print(f"Log base 2 of 8 = {math_operations.log_base_n(8, 2):.4f}")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
