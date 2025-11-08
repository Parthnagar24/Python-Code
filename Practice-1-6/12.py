# Input three numbers and print the largest one (using nested if).


number1 = int(input("Enter 1 number:")) #10
number2 = int(input("Enter 2 number:")) #20
number3 = int(input("Enter 3 number:")) #30

if number1 > number2:         # 10 > 20  F
    if number1 > number3:     # 10 > 30 F
        print("The largest number is:", number1)
    else:         
        print("The largest number is:", number3)  # 30
else:
    if number2 > number3: # 20 > 30 F
        print("The largest number is:", number2)
    else:
        print("The largest number is:", number3) #30

