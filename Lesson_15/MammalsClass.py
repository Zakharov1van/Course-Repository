from AnimalsClass import Animals


class Mammals(Animals):
    def __init__(self, species, habitat, sound, fur_color, domesticated):
        super().__init__(species, habitat, sound)
        self._fur_color = fur_color
        self.domesticated = domesticated

    @staticmethod
    def have_milk():
        print(f"Yes, all mammals have milk.")

    @property
    def fur_color(self):
        return self._fur_color

    @fur_color.setter
    def fur_color(self, new_color: str):
        self._fur_color = new_color

    def is_domesticated(self):
        if self.domesticated:
            print(f"Yes, {self.species} can be domesticated.")
        else:
            print(f"No, {self.species} can't be domesticated.")
