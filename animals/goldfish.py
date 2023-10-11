from movements import Swimming
from .animal import Animal

class Goldfish(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)


    def __str__(self):
        return f"{self.name} is a {self.species}"