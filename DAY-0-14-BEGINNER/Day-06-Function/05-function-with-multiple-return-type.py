# FUNCTION WITH MULTIPLE RETURN VALUES


def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div  # Returns a tuple of 4 values

results = calculate(10, 2)
print("Addition:", results[0])
print("Subtraction:", results[1])
print("Multiplication:", results[2])
print("Division:", results[3])