year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print(f"\n{year} is a leap year.")
    elif year % 100 != 0:
        print(f"\n{year} is a leap year.")
    else:
        print(f"\n{year} is not leap year.")
else:
    print(f"\n{year} is not leap year.")
