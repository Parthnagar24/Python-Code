# RECURSIVE FUNCTION (function calling itself)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # recursion

print("Factorial of 5 =", factorial(5))
