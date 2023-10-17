import time 


#for loop = a statment that will execute its bnlock of code a limited amount of times
#a while loop is infinite
#a for loop is limited

#i = index

for i in range(10+1):
    print(i)

#the second slot is exclusive so you have to put plus one if you want that second number

#the step (third slot) will count up or down by (insert number here) 

for i in range(50,100+1,2):
    print(i)


for i in "slyzoo":
    print(i)



for seconds in range(10,0,-1):
    
    print(seconds)
    time.sleep(1)
    #the sleep pauses the program for (in this case) for 1 second
print("happy new year!")





