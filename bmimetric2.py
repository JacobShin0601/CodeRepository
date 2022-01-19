weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

bmi = (weight)/(height**2)
bmi = round(bmi, 2)
status_BMI = ""


if (bmi < 18.5):
    status_BMI = "Underweight"
elif (18.5 <= bmi <= 24.9):
    status_BMI = "Normal"
elif (25.0 <= bmi <= 29.9):
    status_BMI = "Overweight"
elif (bmi >= 30):
    status_BMI = "Obese"


print("BMI is: ", bmi, ", Status is ", status_BMI, sep="")