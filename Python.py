#1.Getter and Setter

class vechicle:
    def __init__(self,brand,wheel,mileage):
        self.brand = brand
        self.__wheel = wheel
        self.mileage = mileage

    def get_no_of_wheel(self):
        return self.__wheel

    def set_no_of_wheel(self,wheel):
        self.__wheel = wheel

car1 = vechicle("Victara",4,25)

print("No of Wheel : ",car1.get_no_of_wheel())

car1.set_no_of_wheel(6)

print("After set no.of Wheel is : ",car1.get_no_of_wheel())