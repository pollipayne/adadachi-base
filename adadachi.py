from constants import *

class Adadachi:
    def __init__(self,name, personality):
        self.name = name
        self.hunger = 2
        self.happiness = 1
        self.personality = personality
        self.poop_lvl = 0

    def increase_happiness(self, trait):
        if self.happiness >= 10 and self.hunger >= 10 and self.poop_lvl == 0:
            print(f"{self.name} is completely fulfilled! You WON!!")
            print(DANCE_PARTY)
        elif trait >= 10:
            print(f'{self.name} is as happy as they can be! Try fulfilling their other needs.')

        else:
            trait += 1
            print(f"{self.name}'s {trait} level increased from {trait -1}  to {trait}.")

        return self.happiness


    def favorite_increase_happiness(self, trait):
        if self.happiness >= 10 and self.hunger >= 10 and self.poop_lvl == 0:
            print(f"{self.name} is completely fulfilled! You WON!!")
            print(DANCE_PARTY)
        elif trait >= 10:
            print(f'{self.name} is as happy as they can be! Try fulfilling their other needs.')
        else:
            trait += 2
            print(f"{self.name}'s {trait} level increased from {(trait -2)}  to {trait}.")

        return self.happiness
    
    def decrease_happiness(self, trait):
        if trait > 0:
            trait -= 1
            print(f"{self.name}'s {trait} level decreased from {(trait + 1)}  to {trait}.")

        else:
            print(f"{self.name} is so sad it doesn't want to play anymore." )
            print(LOST)


