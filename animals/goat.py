from datetime import date
from movements import Walking
from .animal import Animal

class Goat(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift


    def feed(self):
        print(f'{self.name} was sung Billie Jean and fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"
