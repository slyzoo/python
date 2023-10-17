#if statment = a block of code that will execute if its condition is true

age = int(input("how old are you?: "))


#the dual equal sign is the comparison operator for equality, if you use one equal sign that is the assignment operator and python think you are trying to make age equal to 100
if age == 100:
    print("you are a century old! and also an adult!")

elif age >= 18:
    print("you are an adult!")

elif age <0:
    print("you are not real!!")

else:
    print("you are a child!")
    
