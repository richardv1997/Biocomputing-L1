# Python compound interest calulator #

principle = 0
rate = 0
time =0

while principle <= 0:
    principle= float(input("Enter your principle amount:"))
    if principle <=0:
        print("principle can't be 0 or less than 0 ")

while rate <= 0:
    rate= float(input("Enter your rate amount in %:"))
    if rate <=0:
        print("rate can't be 0 or less than 0 ")

while time <= 0:
    time= float(input("Enter your time in years:"))
    if time <=0:
        print("time can't be 0 or less than 0 ")

print(principle)
print(rate)
print(time)

