# Count how many vowels are in a given string (use loop + if).

text = input("Enter a string: ")  #Enter a string: Hello 
 
count = 0   
for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)




#Number of vowels: 2