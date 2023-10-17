

weight = float(input("wut is your weight? : "))
unit = input("kilograms or pounds (K or L) : ")

if unit == "K":
    weight = weight * 2.205
    unit = "Kgs."

elif unit == "k":
    weight = weight * 2.205
    unit = "Kgs."
    
elif unit == "L":
    weight = weight / 2.205
    unit = "Lbs."

elif unit == "l":
    weight = weight / 2.205
    unit = "Lbs."


else:
    print(f" {unit} is not valid")

print(f" your weight is {round(weight, 2)} {unit}")

