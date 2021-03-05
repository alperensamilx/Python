name = input('Please enter name:\n')
height = float(input("Please enter height in m:\n"))
weight = float(input("Please enter weight in kg:\n"))

bmi = round(weight / height**2, 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    (print(f'Your bmi is {bmi}, you are clinically obese.'))