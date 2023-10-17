#list = used to store multiple items in asingle variable 

food = ["pizza","hamburgers","sausage","chicken alfredo","chocolate pudding"]

food[0] = "chicken parm"

#says the second (lastest) list made
print(food[0])
print(food[1])
print(food[2])
print(food[3])
print(food[4])

#adds another thing to the list
food.append("ice cream")

#removes a thing from the list
food.remove("sausage")

#removes the last element from the list
food.pop()

#inserts a thing inside
food.insert(0,"cake")

#sorts the list alphabetically
food.sort()

#clears the list
food.clear()


#says the first list
for x in food:
    print(x)





