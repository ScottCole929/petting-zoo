from movements import Swimming
from .animal import Animal

class Alligator(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    def swim(self):
        print(f'{self} swims fast')
    
    def __str__(self):
        return f'{self.name} the Alligator'