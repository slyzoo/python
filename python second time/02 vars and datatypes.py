# variable is a reuseable container for storing a value, a variable behaves as if it was the value it contains

#f strings

age = 16

# you cant do this in python    |
#                               V
# print("you are "+ age +" years old")

print('f strings : ')

print("you are "+ str(age) +" years old (v1)")

# this is the correct way to do this ^ in python

#                                  |
# another easier way to do this is V
# in this one it automatically does the spaces for you so you do not need to add them

print("you are", age ,"years old (v2)")

#                                                             |
 #another way to do this exact thing but in the str itself is V
# idk wut a "fstr" is but its becoming popular and handy so i might use that more
#  
print(f"you are {age} years old (v3)")



# integer (int)
# ints are whole numbers like 1, 2, 3, 4...

#age = 16 remember
players = 2
quantity = 5

print('integers : ')

print(f"you are {age} years old v3")
print(f"there are {players} people online")
print(f"you would like to buy {quantity} items")

#float
# a number that contains a decimal like 1.1, 1.2, 1.3, 1.4...


gpa = 3.2
distance = 2.5
price = 10.99

print("float : ")

print(f'your gpa is {gpa}')
print(f'the distance from the store is {distance} miles')
print(f'the price for the can of coke is ${price}')

# string (str)
# a series of text / characters like a, b, @, ^...

name = "slyzoo"
food = "chicken alfredo"
email = "yourneighbourlyhoodfem@gmail.com"
numbers = "1212"
# these strs can be single or double quotes it doesnt matter

print("strings : ")

print(f"hello {name}")
print(f"your fav food is {food}")
print(f"your email is {email}")
print(f"here are random numbers {numbers}")


#boolean
# True or False

online = True
for_sale = True
running = False

print(f"your friend is online : {online}")
print(f"is this for sale? owner {for_sale}")
print(f"am i running? {running}")

# if statment bc why not

if running:
    print ("the game is running")
else:
    print("the game is not running")

# you could write this |
#                      V
a = 1
b= 2 
c = 3

print(a)
print(b)
print(c)

#or you do it like this |
#                       V

x, y, z = 1,2,3
# they still mean the same
print(x)
print(y)
print(z)


d = e = f = 0
# d e and f all = 0
print(d)
print(e)
print(f)

