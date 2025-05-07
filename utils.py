# Exemplary calculator functions

"""Calculator functions"""


def add(a: int, b: int) -> int:
    """Adds two integers"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts one integer from another"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiplies one integer by another"""
    return a * b


def divide(a: int, b: int) -> float:
    """Divides one integer by another. Returns float"""
    return a / b

def to_binary(a) -> int:
    """Converts a number to binary."""
    if (not isinstance(a, int) or not 0 <= a <= 100):
        return -1
    
    res = ''
    while a > 0:
        res = str(a & 1) + res
        a >>= 1
    
    return int(res)