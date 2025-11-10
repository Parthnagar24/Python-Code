# Welcome to Tip Calculator

bill = float(input("Enter the amount:"))
tip = int(input("Enter the amount of tip - $10, $15,$20 :"))
people=int(input("Enter number of people:"))

# bill + tip

tip_bill = bill + (tip /100 * bill)

# tip_bill divide among person
total_bill = tip_bill / people

# round of 2 decimal place
print(round(total_bill,2))

