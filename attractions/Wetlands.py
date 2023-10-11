from .attractions import Attraction
from movements import Swimming

class Wetlands(Attraction):

    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)
        self.animals = list()
    
    def new_animal(self, animal):
        self.animals.append(animal)

    def new_animal_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError:
            print(f'{animal} doesn\'t go in {self.attraction_name}.')

    # @property
    # def last_critter_added(self):
    #     return self.animals[-1]