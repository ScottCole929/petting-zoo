from movements import Swimming, Walking
from .animal import Animal

class Mallard(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
    
    def honk(self):
        print("The mallard honks. A lot")


    def __str__(self):
        return f"{self.name} is a {self.species}"