from movements import Walking
from .attractions import Attraction

class PettingZoo(Attraction):

    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)
        self.animals = list()

    def new_animal(self, animal):
        self.animals.append(animal)

    def new_animal_type_check(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f'{animal} should not be put in {self.attraction_name}')

    # def new_animal_pythonic(self, animal):
    #     try:
    #         if animal.walk_speed > -1:
    #             self.animals.append(animal)
    #             print(f"{animal} now lives in {self.attraction_name}")
    #     except AttributeError as ex:
    #         print(f'{animal} doesn\'t like to be petted, so please do not put in the {self.attraction_name} attraction')

    # @property
    # def last_critter_added(self):
    #     return self.animals[-1]
