def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers. Raises an error if division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 and 3:", subtract(5, 3))
    print("Multiplication of 5 and 3:", multiply(5, 3))
    print("Division of 5 by 3:", divide(5, 3))
