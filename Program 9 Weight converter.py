# Weight converter for Metals
# grams or troy ounces


print("Welcome to the Grams/ troy ounces converter")
print("Please enter the unit type:")

weight= float(input("Please enter your weight: "))

unit= input("Please enter the unit type grams (g) or troy ounce (toz):")





if unit == "g" :
    result= input*0.0321507
    unit= "toz"
    print(f")Your weight is {round(result,3) } {unit}")

elif unit == "toz":
    result= input/0.0321507
    unit = "g"
    print(f"Your weight is {round(result,3) } {unit}gram")

else:
    print(f"{unit} is not a valid unit")




