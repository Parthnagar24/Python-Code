#Input a number and print whether it is positive, negative, or zero.

number = int(input("Enter the number:"))

if number >0:
    print("+ve")
elif number <0:
    print("-ve")
elif number == 0:
    print("Zero")
else:
    print("Invalid input")