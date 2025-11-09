# Functions with more than 1 input

# 'name' and 'location' are parameters.
# The function uses these two values to print a message.
def greet_with(name, location):
    print(f"Hello {name}, see you at {location}!")
#Function Call using Positional Arguments
# The order in which arguments are passed *matters*.
# "Parth" → goes to 'name'
# "Paris" → goes to 'location'
greet_with("Parth", "Paris")   # Output: Hello Parth, see you at Paris!




#Function Definition with Default Values
# Here, 'name' and 'location' have default values.
# If the caller doesn’t provide any argument, these default values are used.
def greet_with_para(name="Parth", location="Paris"):
    print(f"Hello {name}, see you at {location}!")

#Function Call using Default Values
# No arguments are passed, so the defaults ("Parth" and "Paris") are used.
greet_with_para()    # Output: Hello Parth, see you at Paris!


# 🔹 Notes:
# - Positional Arguments → Order matters (first → name, second → location)
# - Keyword Arguments → You can specify directly by name (order doesn’t matter)
# - Default Values → Used when you don’t pass any argument for that parameter