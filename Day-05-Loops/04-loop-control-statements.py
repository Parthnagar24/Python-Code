print("\nExample 5: break statement (stop loop early)")
for num in range(1, 10):
    if num == 5:
        print("Loop stopped at:", num)
        break  # stops the loop completely
    print(num)

print("\nExample 6: continue statement (skip one iteration)")
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3")
        continue  # skips this iteration
    print("Number is:", num)

print("\nExample 7: pass statement (placeholder - does nothing)")
for num in range(1, 4):
    if num == 2:
        pass  # 'pass' just means do nothing here
    print("Processing number:", num)
