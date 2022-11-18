from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def Tyre(self):
        pass
    #@staticmethod
    def Speed(self):
        print("Vehicle Speed is Avg.:- 100km")
class Car(Vehicle):
    def Speed(self):
        super().Speed()
        print("Car Speed is 140km")
    def __init__(self):
        print("Show the init function.")
    def __del__(self):
        print("init has been deleted.....")
    def Tyre(self):
        print("Car Tyre is 4.")
class Bike(Vehicle):
    def Speed(self):
        print("Bike Speed is 160km")
    def Tyre(self):
        print("Bike tyre is 2.")

b1=Bike()
c1=Car()
c2=Car()
b1.Tyre()
c1.Tyre()
c1.Speed()
b1.Speed()
del c2
#print(c1)


