# FUNCTION WITH **KWARGS (keyword arguments)


def student_details(**info):
    for key, value in info.items():
        print(key, ":", value)

student_details(name="Parth", age=20, course="Python")