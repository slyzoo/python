import math
from multiprocessing.spawn import import_main_path


import_main_path

pi = -3.14
x = 1
y = 2
z = 3
#rounds to the nearest number
print(round(pi))

#rounds to the next highest number
print(math.ceil(pi))

#rounds to the next lowest number
print(math.floor(pi))

#gives you the absolute value of that number
print(abs(pi))

#will raise to the power of (insert number here)
print(pow(pi,2))

#does the square root of the selected number
print(math.sqrt(420))

#will give you the highest value of the selected numbers
print(max(x, y, z))

#will give you the lowest value of the selected numbers
print(min(x, y, z))