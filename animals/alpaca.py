from movements import Walking
from .animal import Animal

class Alpaca(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
    

    def __str__(self):
        return f"{self.name} is a {self.species}"