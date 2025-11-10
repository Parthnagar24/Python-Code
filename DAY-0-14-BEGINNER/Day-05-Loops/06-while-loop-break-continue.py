print("\nExample 9: While loop with break and continue")
num = 0
while True:
    num += 1
    if num == 3:
        print("Skipping 3")
        continue
    if num > 5:
        print("Breaking loop at", num)
        break
    print("Number is:", num)
