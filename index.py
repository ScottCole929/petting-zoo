from animals import Alligator, Goose, Boa, Cobra, Copperhead, Mamba, RatSnake, Dolphin, Goldfish, Mallard, Piranha, Shark, Alpaca, Donkey, Goat, Llama, Sheep
from attractions import PettingZoo, SnakePit, Wetlands

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 35)
miss_fuzz = Llama("Miss Fuzz", "llama", "afternoon", "pizza", 24)
hee_haw = Donkey("Hee Haw", "donkey", "morning", "steak", 367)
billy = Goat("Billy", "goat", "afternoon", "broccoli", 94)
curly = Sheep("Curly", "sheep", "midday", "burgers", 2012)
tina = Alpaca("Tina", "alpaca", "morning", "watermelon", 723)
bitey = Copperhead("Bitey", "copperhead", "eggs", 925637)
jafar = Cobra("Jafar", "cobra", "beef", 2389)
nice_boy = RatSnake("Nice Boy", "rat snake", "hummus", 745)
squeezebox = Boa("Squeezebox", "boa constrictor", "cauliflower", 2875)
kill_bill = Mamba("Kill Bill", "black mamba", "ribs", 94)
sir_quackington = Mallard("Sir Quackington", "mallard", "bread", 9076)
rainbow = Goldfish("Rainbow", "goldfish", "chicken", 234)
nomnom = Piranha("Nom Nom", "piranha", "chocolate", 9374)
jaws = Shark("Jaws", "shark", "nachos", 4567)
flipper = Dolphin("Flipper", "dolphin", "pasta", 2569)
dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Alligator("Snappy", "American Alligator", "fish", 1044)

varmint_village = PettingZoo("Varmint Village", "Land dwelling animals to pet")
slither_inn = SnakePit("Slither Inn", "Anything that slides along without legs")
critter_cove = Wetlands("Critter Cove", "Water based animals found here")

varmint_village.new_animal(miss_fuzz)
varmint_village.new_animal(hee_haw)
varmint_village.new_animal(billy)
varmint_village.new_animal(curly)
varmint_village.new_animal(tina)
varmint_village.new_animal(bob)
slither_inn.new_animal(bitey)
slither_inn.new_animal(jafar)
slither_inn.new_animal(nice_boy)
slither_inn.new_animal(squeezebox)
slither_inn.new_animal(kill_bill)
critter_cove.new_animal(sir_quackington)
critter_cove.new_animal(rainbow)
critter_cove.new_animal(nomnom)
critter_cove.new_animal(jaws)
critter_cove.new_animal(flipper)


# print(f'{slither_inn.attraction_name} is the place to find {", ".join(f"{animal.name} the {animal.species}" for animal in slither_inn.animals)}.')
# print(f'{critter_cove.attraction_name} is the place to find {", ".join(f"{animal.name} the {animal.species}" for animal in critter_cove.animals)}.')

# bitey.chip_number = 34
# print(bitey.chip_number)

# print(critter_cove.last_critter_added)

# squeezebox.feed()
# billy.feed()
# nomnom.feed()

# bob.run()
# bob.swim()

# for animal in varmint_village.animals:
#     print(animal)

varmint_village.new_animal_type_check(dolly)
varmint_village.new_animal_type_check(snappy)

slither_inn.new_animal_type_check(hee_haw)
slither_inn.new_animal_type_check(kill_bill)

critter_cove.new_animal_pythonic(rainbow)
critter_cove.new_animal_pythonic(nice_boy)
