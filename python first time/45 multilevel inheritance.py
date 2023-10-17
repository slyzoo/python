#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#---------------------------------------------------------------------------------------------------

#mulitlevel inheritance = when a derived (child) class inherits another derived (child) class



class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("i do indeed eat")

class Dog(Animal):
    def bark(self):
        print("BARK")

    def woof(self):
        print("woof")

dog = Dog()
print(dog.alive)

dog.bark()
dog.eat()











