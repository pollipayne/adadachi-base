from constants import *

class Adadachi:
    def __init__(self,name, personality):
        self.name = name
        self.hunger = 2
        self.happiness = 1
        self.personality = personality
        self.poop_lvl = 0

    def increase_happiness(self):
        if self.happiness >= 10 and self.hunger >= 10 and self.poop_lvl == 0:
            print(f"{self.name} is completely fulfilled! You WON!!")
            print(DANCE_PARTY)
        elif self.happiness >= 10:
            print(f'{self.name} is as happy as they can be! Try fulfilling their other needs.')

        else:
            self.happiness += 1
            print(f"{self.name}'s happiness level increased from {self.happiness -1}  to {self.happiness}.")

        return self.happiness


    def favorite_increase_happiness(self):
        if self.happiness >= 10:
            print(f'{self.name} is as happy as they can be! Try fulfilling their other needs.')
        else:
            self.happiness += 2
            print(f"{self.name}'s happiness level increased from {(self.happiness -2)}  to {self.happiness}.")

        return self.happiness
    
    def decrease_happiness(self):
        if self.happiness > 0:
            self.happiness -= 1
            print(f"{self.name}'s happiness level decreased from {(self.happiness + 1)}  to {self.happiness}.")

        else:
            print(f"{self.name} is so sad it doesn't want to play anymore." )
            print(LOST)


