
unit = input("is this temperature in Celsius (C) or Fahrenheit (F)? : ")
temp = float(input("enter the temperature : "))

#Celsius (C)
if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(temp)
    print(f"the temp in Celsius (C) is {temp}")
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(temp)
    print(f"the temp in Celsius (C) is {temp}")

#Fahrenheit (F)
elif unit == "f":
    temp = round((temp - 32) * 5/9, 1)
    print(temp)
    print(f"the temp in Fahrenheit (F) is {temp}")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(temp)
    print(f"the temp in Fahrenheit (F) is {temp}")

else:
    print(f"{unit} is invalid")
