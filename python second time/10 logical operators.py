# logical operators are used in conditional statments

# "and" checks if two or more conditions are true
# "or" checks if at least on condition is true
# "not" if True then the condition is false, the same is the other way around too


temp_1 = 25
temp_2 = 40
sunny = True

# and
if temp_1 >0 and temp_1 <30:
    print("temp is good")
else:
    print("the temp is bad")

# or
if temp_2 <=0 or temp_2 >= 30:
    print("bad weather")
else:
    print("good weather")

# not
if sunny == True:
    print("go outside, it's sunny out")
else:
    print("it is cloudy outside")
# or do this
if sunny:
    print("go outside, it's sunny out")
else:
    print("it is cloudy outside")
# or do this
if not sunny:
    print("it is cloudy outside")
else:
    print("it is sunny outside")