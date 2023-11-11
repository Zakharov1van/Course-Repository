from MammalsClass import Mammals


class Predators(Mammals):
    def __init__(self, species: str, habitat: str, _fur_color: str, sound: str,
                 domesticated: bool, omnivore: bool):
        super().__init__(species, habitat, sound, _fur_color, domesticated)
        self.omnivore = omnivore
        self.dangerous_carnivores = ["Lion", "Tiger", "Leopard", "Crocodile", "Polar Bear", "Grizzly Bear",
                                     "African Cape Buffalo", "Hyena", "Wolf"]
        self.list_of_prey = []

    def is_dangerous(self):
        if self.species in self.dangerous_carnivores:
            print("Yes, this carnivore is dangerous")
        else:
            print("No, this carnivore is not known to prey on humans")

    def can_eat_vegetation(self):
        if self.omnivore:
            print("Yes, this carnivore can eat vegetation")
        else:
            print("No, this carnivore can't eat vegetation")

    def add_prey(self, prey):
        self.list_of_prey.append(prey)
