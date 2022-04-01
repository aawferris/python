from contextlib import nullcontext

from numpy import empty

print("Welcome to Tip Calculator!")

bill = round(float(input("How much is the bill?\n $ ")), 2)
tip = int(input("What percentage tip would you like to leave? \n %"))
guests = int(input("How many people are splitting the bill? \n"))

percentage = float(float(bill) * tip / 100)
total = round(float(bill + percentage), 2)
split = round(float(total / guests), 2)


def calculate_tip():
    if guests == 0:
        print("You can't have 0 guests! No dine and dash!")
        return
    print(f"Each person should pay ${split}")


calculate_tip()
