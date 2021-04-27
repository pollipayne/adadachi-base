from player import Player
from adadachi import Adadachi
from constants import *
import random

player = Player()

def display(statement):
    print(statement)


def create_adadachi():
    name = input(GET_NAME + "\n\t")
    foods = player.inventory["foods"]
    games = player.inventory["games"]
    personality = {
        "fav_food": random.randint(0,(len(foods)-1)),
        "fav_game": random.randint(0,(len(games)-1)),
        "hates_food": random.randint(0,(len(foods)-1)),
        "hates_game": random.randint(0,(len(games)-1)),
    }
    while personality["fav_food"] == personality["hates_food"] or personality["fav_game"] == personality["hates_game"]:
        personality["fav_food"] = random.randint(0, (len(foods)-1))
        personality["fav_game"] = random.randint(0, (len(foods)-1))

    player.adadachi = Adadachi(name,personality)





def start_game():
    display(TITLE)
    answer = input(GREETING)
    if answer.lower() == "y":
        create_adadachi()
        while player.adadachi.hunger > 0 and player.adadachi.happiness > 0 and player.adadachi.poop_lvl < 10:
            option = input(OPTIONS).lower()

            if option == "s":
                player.get_status()
            elif option == "c":
                    player.clean()
            elif option == "f":
                if player.inventory["foods"]:
                    player.feed()
                else:
                    break
            elif option == "p":
                player.play_with_adadachi()
            elif option == "x":
                return display(EXIT)
        answer = input(LOST)
        if answer.lower() == 'y':
            start_game()
        else:
            display(EXIT)

        