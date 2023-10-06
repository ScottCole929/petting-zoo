class PettingZoo:
    def __init__(self, attraction_name, description, animals):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []
    
    def new_animal(self, animal):
        self.animals.append(animal)

