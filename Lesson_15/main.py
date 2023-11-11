from AnimalsClass import Animals
from MammalsClass import Mammals
from PredatorsClass import Predators


wolf = Predators("Wolf", "Forrest", "Grey", "Bark!!!", False, False)

snake = Animals("Snake", "Sand", "Hiss!!!")
snake.have_milk()
snake.had_kids("Robby")
snake.produce_sound()


cow = Mammals("Cow", "Field", "Mooo!!!", "White", True)
cow.have_milk()
cow.is_domesticated()
cow.fur_color = "Brown"

wolf.produce_sound()
wolf.had_kids("Fluffy")
print(wolf.kids)
wolf.have_milk()
wolf.fur_color = "Black"
wolf.is_domesticated()
wolf.is_dangerous()
wolf.can_eat_vegetation()
wolf.add_prey("Rabbit")
