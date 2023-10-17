import random

#nothing is truly random, this is psudo-random

x = random.randint(1,6)
y = random.random()

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

mylist = ['rock ', 'paper ', 'scissors ']
z = random.choice(mylist)

print(x)
print(y)
print(z)
print(cards)









































