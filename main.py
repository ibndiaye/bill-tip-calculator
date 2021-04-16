print("welcome to my bill calculator")

bill=float(input("what was your total bill? $"))
tip=float(input("how much tip would you like to give? "))
people = int(input("how many people to split the bill? "))
bill_with_tip= tip/100 *bill +bill

# print(bill_with_tip)

bill_per_person = bill_with_tip / people
final_amount=round(bill_per_person,2)
final_amount="{:.2f}".format(bill_per_person)
print(f"each person should pay ${final_amount}.")
