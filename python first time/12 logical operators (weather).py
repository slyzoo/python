#logical operators (and, or, not) = used to check if two or more condional statments are true
#not is 


temp = int(input("what is the temperature outside?: "))

#for the statment to be true BOTH parts have to be true
if temp >= 25 and temp <= 100:
    print("the temperature is good today")
    print("go outside you lazy fuck")

    
elif temp < 0 or temp >100:
    print("the temperature is bad today")
    print("dont go outside")

#or another way to do this is
#
#if not(temp >= 25 and temp <= 100):
#    print("the temperature is bad today")
#    print("dont go outside")
#elif not(temp < 0 or temp >100):
#    print("the temperature is good today")
#    print("go outside you lazy fuck")




