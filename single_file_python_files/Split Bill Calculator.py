#Made as part of the Building As I Learn repository on Github - Created/Submitted 10/20/2023#

total_bill = float(input("What was the total bill? $"))
num_people = float(input("How many people to split the bill? "))
bill_tip = float(input("How much of a tip would you like to give? Choose a reasonable number, decimal or whole. "))
split_payment = round(((total_bill / num_people) * ((bill_tip / 100) + 1)),2)
print(split_payment)
