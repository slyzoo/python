#imports a module / file (in this case math) to the python file
import math



# some things to help with math
a = 3.14

b = -4

c = 5

result1 = round(a) #round to nearest whole number
print(f" round : {result1}")
print("") # so it doesnt look as bad

result2 = abs(b) # absolute value
print(f" absolute value : {result2}")
print("")

result3 = pow(4, 3) # exponent (4 to the power of 3 [4 x 4 x 4])
print(f" exponent : {result3}")
print("")

result4 = max(a, b, c) # finds the max value of the selected
print(f" max : {result4}")
print("")

result5 = min(a, b, c) # finds the min value of the selected
print(f" min : {result5}")
print("")







#math module / file

math.pi
print(f" pi : {math.pi}")
print("")

math.e
print(f" e (for physics) : {math.e}")
print("")

d = 9

result6 = math.sqrt(d)
print(f"square root : {result6}")
print("")


e = 5.4

result7 = math.ceil(e)
print(f"ceiling : {result7}")
print("")

f = 5.8

result8 = math.floor(f)
print(f"floor : {result8}")
print("")