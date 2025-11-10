# FUNCTION WITH DEFAULT PARAMETERS

def greet_with_message(name="Guest"):
    print("Hello", name, "!")
    
greet_with_message()          # Uses default value
greet_with_message("Parth")   # Overrides default value
