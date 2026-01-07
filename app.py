# app.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

if __name__ == "__main__":
    print("Demo Python Application")
    print("Add 2 + 3 =", add(2, 3))
    print("Multiply 4 * 5 =", multiply(4, 5))
    print("Is 10 even?", is_even(10))
