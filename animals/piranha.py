from datetime import date
from movements import Swimming
from .animal import Animal

class Piranha(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
    
    def feed(self):
        print(f'{self.name} was sung Billie Jean and fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


    def __str__(self):
        return f"{self.name} is a {self.species}"