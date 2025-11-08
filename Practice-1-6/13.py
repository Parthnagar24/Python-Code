#Ask for a student’s marks and print:
#≥ 90 → “A Grade”
#75–89 → “B Grade”
#50–74 → “C Grade”
#< 50 → “Fail”

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif marks>=75 and marks<=89:
    print("B")
elif marks>=50 and marks<=74:
    print("C")
else:
    print("Fail")