height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# converted_height = float(height)
# converted_weight = float(weight)

# bmi = (converted_weight / (converted_height ** 2))

# print(int(bmi))

# BMI Calculator 2.0
bmi = round(weight / (height ** 2))

if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi <= 35 and bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi <= 30 and bmi > 25:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 25 and bmi > 18.5:
    print(f"Your BMI is {bmi}, you have a normal weight.")
else:
    print(f"Your BMI is {bmi}, you are underweight.")
