print("\nExample 4: Nested loops - Multiplication Table")
for i in range(1, 4):         # Outer loop
    for j in range(1, 4):     # Inner loop
        print(i, "x", j, "=", i * j)
    print("---- End of Table for", i, "----")