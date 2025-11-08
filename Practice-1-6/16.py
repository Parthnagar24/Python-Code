#Input 5 numbers using a loop, store them in a list, and print the list.

list=[]
for number in range(0,5):
    number = int(input("Enter the number:"))
    list.append(number)

print(list)