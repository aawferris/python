height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

converted_height = float(height)
converted_weight = float(weight)

bmi = (converted_weight / (converted_height ** 2))

print(int(bmi))
