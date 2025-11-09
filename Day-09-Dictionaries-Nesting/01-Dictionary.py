# 1️⃣ Creating a Dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Accessing a value using its key
print(programming_dictionary["Bug"])


# 2️⃣ Adding a New Key-Value Pair

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)
# Output:
# {
#   'Bug': 'An error in a program that prevents the program from running as expected.',
#   'Function': 'A piece of code that you can easily call over and over again.',
#   'Loop': 'The action of doing something over and over again.'
# }



# 3️⃣ Creating an Empty Dictionary

empty_dictionary = {}

# Wipe an existing dictionary (uncomment below to test)
# programming_dictionary = empty_dictionary
# print(programming_dictionary)   # Output: {}



# 4️⃣ Editing an Existing Value

programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)


# 5️⃣ Looping Through a Dictionary


# When you loop through a dictionary, you get the keys by default.
# To get the values, use programming_dictionary[key]
for key in programming_dictionary:
    print(key)                      # prints the key
    print(programming_dictionary[key])  # prints the corresponding value