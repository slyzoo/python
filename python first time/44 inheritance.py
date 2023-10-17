#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#---------------------------------------------------------------------------------------------------


class Animal:

    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

    def breed(self):
        print("this animal is breeding")

#---------------------------------------------------------------------------------------------------

class rabbit(Animal):
    
    def run(self):
        print("this rabbit is  running")

class hawk(Animal):
    def fly(self):
        print("this hawk is  flying")

class fish(Animal):
    def swim(self):
        print("this fish is  swimming")

#---------------------------------------------------------------------------------------------------

#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()













