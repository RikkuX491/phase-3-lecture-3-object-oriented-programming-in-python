import ipdb

class Car:

    def __init__(self, make, year, license_plate, color):
        self.make = make
        self.year = year
        self.license_plate = license_plate
        self.color = color

    def honk_horn(self):
        print("Beep beep!")

    def go(self):
        print("VROOOOM!")

    def get_year(self):
        return self._year
    
    def set_year(self, year):
        if(type(year) == int) and (2000 <= year <= 2023):
            self._year = year
        else:
            raise Exception("Invalid year!")
        
    def get_license_plate(self):
        return self._license_plate
    
    def set_license_plate(self, license_plate):
        if(len(license_plate) == 7):
            self._license_plate = license_plate
        else:
            raise Exception("License Plate must be 7 characters long!")

    year = property(get_year, set_year)
    license_plate = property(get_license_plate, set_license_plate)

car1 = Car("Honda", 2000, "ABC1234", "Red")
car2 = Car("Toyota", 2023, "BCD2345", "Blue")