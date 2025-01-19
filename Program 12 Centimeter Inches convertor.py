#Converter for inch and centimeter
import math

print("This program will convert your measurement from either inchs to cm, or cm to inches")
measurement = float(input("Please enter your measurement:"))
operator = input("Please enter the unit, Inches (in) or Centimeter (cm):")

if operator == "in":
    value = (2.54* measurement)

    operator = "centimeter"
    print(f"Your results is {round(value,2)} {operator}")

elif operator == "cm":
    value = (0.393701* measurement)
    operator = "inches"
    feet = 0.0833333* value
    print(f"Your result: {round(value,2)} {operator}")
    print(f"This is {round(feet,2)}ft ")

else:
    print("Invalid units used.")
