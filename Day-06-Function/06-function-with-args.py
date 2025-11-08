# FUNCTION WITH *ARGS (variable number of arguments)


def show_students(*names):
    print("Student List:")
    for n in names:
        print("-", n)

show_students("Alice", "Bob", "Charlie", "Daisy")