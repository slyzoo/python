#this is a grocery cart program


#the item, price and, quantity
item = input("what item would you like to buy? : ")
price = float(input("what is the price? : "))
quantity = int(input("how many would you like to buy? : "))


#the calculator part
total = price * quantity

#it telling you how much of {item} and telling you the {item}/s and the total
print(f"you have bought {quantity} X {item}/s")
print(f"your total is {round(total, 2)}")
