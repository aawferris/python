age = input("What is your current age? ")

day_age = (90 * 365) - (int(age) * 365)
week_age = (90 * 52) - (int(age) * 52)
month_age = (90 * 12) - (int(age) * 12)

print(
    f"You have {day_age} days, {week_age} weeks, and {month_age} months left.")
