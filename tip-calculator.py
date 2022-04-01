bill = input("How much is the bill?\n")
tip = input("What percentage tip would you like to leave? \n")
guests = input("How many people are splitting the bill? \n")

n_bill = float(bill)
n_tip = float(tip)
n_guests = int(guests)

percentage = (n_bill * n_tip) / 100
total = n_bill + percentage
print(f"the percentage is {percentage} and the total is {total}")


def calculate_tip():
    if guests == 0:
        print("You can't have 0 guests! No dine and dash!")
        return
    split = total / n_guests
    print(f"Each person should pay ${split}")


calculate_tip()
