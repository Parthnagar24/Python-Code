print("\nExample 8: Sum of even numbers between 1 and 10")
total = 0
for num in range(1, 11):
    if num % 2 == 0:
        total += num
print("Sum of even numbers = ", total)