# lets make a logic for riding monster truck for BOB is valid or not with help of his age and height

 
height = int(input("Enter the height of Person in cm:"))

if height > 200 :
    age = int(input("Enter the age of the person:"))
    if age > 25 :
        print("IS valid to ride a monster truck!")
    else:
        print("IS not valid to ride a monster truck!")
else:
    print("Grow your height to ride a monster truck!")