from movements import Slithering
from .attractions import Attraction

class SnakePit(Attraction):

    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)
        self.animals = list()
    
    def new_animal(self, animal):
        self.animals.append(animal)
    
    def new_animal_type_check(self, animal):
        if isinstance(animal, Slithering):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f'{animal} should not be put in {self.attraction_name}')
    
    # @property
    # def last_critter_added(self):
    #     return self.animals[-1]