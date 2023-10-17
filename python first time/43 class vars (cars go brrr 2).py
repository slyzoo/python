#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#---------------------------------------------------------------------------------------------------


class Car:

    wheels = 4 #class var
    
    def __init__(self,make,model,year,colour):
        self.make = make    #instance var
        self.model = model    #instance var
        self.year = year    #instance var
        self.colour = colour    #instance var


    def drive(self):
        print("this "+self.model+" is driving ")

    def stop(self):
        print("this "+self.model+" is stopped ")

#---------------------------------------------------------------------------------------------------


car_1 = Car("ford","f150",2020,"purple")
car_2 = Car("nissan", "altima", 2013, "gray")

car_1.wheels = 2


print(car_1.wheels)
print(car_2.wheels)


print(Car.wheels)

















