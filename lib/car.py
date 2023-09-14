import ipdb

class Car:
    
    def __init__(self, make, model, year, horn_volume = 1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year_parameter):
        if (type(year_parameter) == int) and (1900 <= year_parameter <= 2023):
            self._year = year_parameter
        else:
            raise ValueError("Year must be an integer and must be between 1900 and 2023!")
        
    @property
    def horn_volume(self):
        return self._horn_volume
    
    @horn_volume.setter
    def horn_volume(self, horn_volume_parameter):
        if type(horn_volume_parameter) == int:
            self._horn_volume = horn_volume_parameter
        else:
            raise ValueError("Horn volume must be an integer!")

    def get_make(self):
        return self._make
    
    def set_make(self, make):
        if (type(make) == str) and (len(make) >= 3):
            self._make = make
        else:
            raise ValueError("make must be a string and must be at least 3 characters long!")

    make = property(get_make, set_make)

    def honk_horn(self):
        print(f"BEEP BEEP{'!' * self.horn_volume}")

ipdb.set_trace()