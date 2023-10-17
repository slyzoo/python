# if statments, they do some code IF some condition is True 
# else statments, they do something else


age = int(input("Enter your age : "))

# only ONE if statment is allowed
# if the age is greater an 200, then say "you are now signed up"
if age >= 120: 
    print("you're too old to sign up, and how are you alive?")

# you can put as many elif statments as you want
# if the age is less than 0 then say "you arent born yet"
elif  age >= 18: 
    print("you are now signed up")


elif age < 0:
    print("you aren't born yet")

# only ONE else statment is allowed
# if the age is anything else then say "you must be 18+ to sign up"
else:
    print("you must be 18+ to sign up")


