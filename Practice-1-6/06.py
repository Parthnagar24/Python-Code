# Input two numbers, convert them to integers, and print:
#Sum Difference Product Division (rounded to 2 decimal places using round())

number1 = float(input("Enter 1 number:"))
number2 = float(input("Enter 2 number:"))

sum = number1+number2
diff = number1-number2
product = number1*number2
division = (number1/number2)

print(sum)
print(diff)
print(product)
print(division)

print(round(sum,2))
print(round(diff,2))
print(round(product,2))
print(round(division,2))


#Enter 1 number:10.1256556
#Enter 2 number:5.65566555
#15.78132115
#4.46999005
#57.26732154808458
#1.790356150037903
#15.78
#4.47
#57.27
#1.79