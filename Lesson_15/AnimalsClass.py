class Animals:
    def __init__(self, species: str, habitat: str, sound: str):
        self.species = species
        self.habitat = habitat
        self.sound = sound
        self.kids = []

    def produce_sound(self):
        print(self.sound)

    def had_kids(self, name_of_kid: str):
        self.kids.append(name_of_kid)

    @staticmethod
    def have_milk():
        print("Only mammals have milk.")
