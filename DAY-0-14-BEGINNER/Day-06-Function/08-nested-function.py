#  NESTED FUNCTIONS (function inside another)


def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()  # Call inner function

outer()