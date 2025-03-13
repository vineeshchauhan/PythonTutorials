import random

class Dice:
    def roll(self):
        f = random.randint(1,6)
        s = random.randint(1, 6)
        return f,s


dice = Dice()
print(dice.roll())