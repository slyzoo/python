# method chaining = calling multiple methods sequentially, each call preforms an action on the same object and returns self



class Car:
    def turn_on(self):
        print("this car is turned on")
        return self

    def drive(self):
        print("this car is driving")
        return self

    def brake(self):
        print("this car is braked")
        return self

    def turn_off(self):
        print("this car is turned off")
        return self




car = Car()

# so these do the same thing but the second one does it in less lines of code meaning it is better
car.turn_on()
car.drive()

car.turn_on().drive()

car.brake().turn_off()

car.turn_on().drive().brake().turn_off()


# \ is a line continueation character
# it just makes it more readable
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

