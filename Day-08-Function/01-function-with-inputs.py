# Example 1 - Functions without input 

# Function definition
# 'def' keyword is used to define a function.
# This function does not take any input and simply prints messages.
def greet():                      
    print("Hello, How are you?")
    print("What's the time now?")
    print("Guten Morgan")   # German for "Good Morning"

# Function call
# When we call the function using its name followed by parentheses,
# Python jumps to the function definition and executes its body.
greet()


# Example 2 - Function with input 

# Function definition with a parameter
# 'name' here is a parameter — it acts like a placeholder variable 
# that will hold the value passed to the function.
def greet_someone(name):
    print(f"Hello, {name}! How do you do?")

# Function call with an argument
# 'Parth' is the argument — the actual value being passed into the function.
# When called, the function replaces 'name' with "Parth" during execution.
greet_someone("Parth")

# 🔹 Notes:
# Parameter → variable name used in the function definition (e.g., name)
# Argument  → actual data/value passed when calling the function (e.g., "Parth")

