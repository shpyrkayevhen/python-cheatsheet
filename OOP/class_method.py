import random

# representing sorting hat from class method


class Hat:

    # class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name: str):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
