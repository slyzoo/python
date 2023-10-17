#multiple inheritance = when a child class is derived from more than one parent class


class Prey:
    def flee(self):
        print("this animal is fleeing")

class Predator:
    def hunt(self):
        print("this animal is hunting")



class Rabbit (Prey):
    print("hop")

class Hawk (Predator):
    print("*screeeches*")


class Fish(Prey,Predator):
    print("i fish")


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

