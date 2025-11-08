# -----------------------------------------------------------
# 🧠 FUNCTIONS IN PYTHON - COMPLETE EXAMPLES WITH COMMENTS
# -----------------------------------------------------------

# -----------------------------------------------
# 1️⃣ BASIC FUNCTION
# -----------------------------------------------

# Defining a simple function (no parameters)
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()


# -----------------------------------------------
# 2️⃣ FUNCTION WITH PARAMETERS
# -----------------------------------------------

def greet_user(name):
    print("Hello,", name, "nice to meet you!")

greet_user("ng24")  # Function call with argument


# -----------------------------------------------
# 3️⃣ FUNCTION WITH RETURN VALUE
# -----------------------------------------------

def add_numbers(a, b):
    result = a + b
    return result  # Sends the result back to the caller

sum_result = add_numbers(5, 10)
print("Sum is:", sum_result)


# -----------------------------------------------
# 4️⃣ FUNCTION WITH DEFAULT PARAMETERS
# -----------------------------------------------

def greet_with_message(name="Guest"):
    print("Hello", name, "!")
    
greet_with_message()          # Uses default value
greet_with_message("Parth")   # Overrides default value


# -----------------------------------------------
# 5️⃣ FUNCTION WITH MULTIPLE RETURN VALUES
# -----------------------------------------------

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


# -----------------------------------------------
# 6️⃣ FUNCTION WITH *ARGS (variable number of arguments)
# -----------------------------------------------

def show_students(*names):
    print("Student List:")
    for n in names:
        print("-", n)

show_students("Alice", "Bob", "Charlie", "Daisy")


# -----------------------------------------------
# 7️⃣ FUNCTION WITH **KWARGS (keyword arguments)
# -----------------------------------------------

def student_details(**info):
    for key, value in info.items():
        print(key, ":", value)

student_details(name="Parth", age=20, course="Python")


# -----------------------------------------------
# 8️⃣ NESTED FUNCTIONS (function inside another)
# -----------------------------------------------

def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()  # Call inner function

outer()


# -----------------------------------------------
# 9️⃣ LAMBDA (anonymous or one-line function)
# -----------------------------------------------

# Syntax: lambda arguments : expression
square = lambda x: x * x
print("Square of 5 is:", square(5))

# Another example with multiple arguments
add = lambda a, b: a + b
print("Sum using lambda:", add(3, 7))


# -----------------------------------------------
# 🔟 RECURSIVE FUNCTION (function calling itself)
# -----------------------------------------------

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # recursion

print("Factorial of 5 =", factorial(5))


# -----------------------------------------------
# ✅ END OF FUNCTION EXAMPLES
# -----------------------------------------------
