import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def log(x, base=10):
    if x <= 0:
        raise ValueError("log input must be > 0")
    if base <= 0 or base == 1:
        raise ValueError("log base must be > 0 and != 1")
    return math.log(x, base)


def square(x):
    return x * x


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def sqrt(x):
    if x < 0:
        raise ValueError("sqrt input must be >= 0")
    return math.sqrt(x)


def percent(x):
    return x / 100
