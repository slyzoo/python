import math

radius = float(input("enter the radius of the circle : "))

# A = pi * r^2

Area = math.pi * pow(radius, 2)

print(f"The area is : {round(Area, 4)}")