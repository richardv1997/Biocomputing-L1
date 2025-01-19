# Temperature converter Celsius/ Fahrenheit

unit= input("Is this temperature in Celsuis (c) or Fahrenheit (f) :")
temperature = float(input("Please enter the temperature:"))


if unit== "c":
    result = ((temperature * 9)/5 + 32)
    unit = "F"
    print(f"The temperature is {round(result,1)} {unit}")
elif unit== "f":
    result = ((temperature-32)/1.8)
    unit= "C"
    print(f"The temperature is {round(result,1)} {unit}")
else:
    print(f"{unit} is an invalid unit")