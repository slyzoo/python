#you can have classes in and outside of this file

# P.O.O.P. stands for Python Object Oriented Programming

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#---------------------------------------------------------------------------------------------------

class Car:
    def __init__(self,make,model,year,colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour


    def drive(self):
        print("this "+self.model+" is driving ")

    def stop(self):
        print("this "+self.model+" is stopped ")

#---------------------------------------------------------------------------------------------------

#car_1 = Car("make","model","year","colour")

car_1 = Car("ford","f150",2020,"purple")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)

car_1.drive()
car_1.stop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


car_2 = Car("nissan", "altima", 2013, "gray")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)

car_2.drive()
car_2.stop()

print(car_1.make)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~