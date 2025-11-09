#Print a multiplication table for any number entered by the user.

number = int(input("Enter the number:"))

for i in range(1,11):
    print(number,"*",i,"=",number*i)

#Enter the number:6
#6 * 1 = 6
#6 * 2 = 12
#6 * 3 = 18
#6 * 4 = 24
#6 * 5 = 30
#6 * 6 = 36
#6 * 7 = 42
#6 * 8 = 48
#6 * 9 = 54
#6 * 10 = 60