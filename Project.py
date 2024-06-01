#Calculator project.

print("Welcome to the tip calculator!")

bill=float(input("What was the total bill? $"))
print(bill)

tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
print(tip)
people=int(input("How many people to split the bill?"))


#bill_with_tip=bill * (1+tip/100)
#Or
#bill_with_tip=tip/100 * bill + bill
#print(bill_with_tip)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount=round(bill_per_person)

print(f"Each person should pay: ${final_amount}")
