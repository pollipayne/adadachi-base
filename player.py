
from constants import STATUS
import random

class Player:
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }

    def play_with_adadachi(self):
        player_game_choice = input(f'''
**************************************************
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^                                                ^
              What game would you like           
^                  to play with                  ^
                  {self.adadachi.name}?:            
^                 ============                   ^
         "A" for {self.inventory['games'][0]}                               
^                                                ^
         "B" for {self.inventory['games'][1]}  
^                                                ^
         "C" for {self.inventory['games'][2]}    
^                                                ^
         "D" for {self.inventory['games'][3]}                                                
**************************************************
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''')
        while player_game_choice:
            if player_game_choice.lower() == "a":
                game_choice = self.inventory['games'][0]
                self.game_result(game_choice)
                break
            elif player_game_choice.lower() == "b":
                game_choice = self.inventory['games'][1]
                self.game_result(game_choice)
                break
            elif player_game_choice.lower() == "c":
                game_choice = self.inventory['games'][2]
                self.game_result(game_choice)
                break
            elif player_game_choice.lower() == "d":
                game_choice = self.inventory['games'][3]
                self.game_result(game_choice)
                break
            else:
                player_game_choice = input("Please make a valid selection:  ")

    def game_result(self, game_choice):
        adadachi_hates = self.inventory['games'][self.adadachi.personality["hates_game"]]
        adadachi_fav = self.inventory['games'][self.adadachi.personality["fav_game"]]
        if adadachi_hates == game_choice:
            print(f"You played {game_choice} with {self.adadachi.name} but that is \
their least favorite game! Whomp Whomp!")
            self.adadachi.decrease_happiness()
        elif adadachi_fav == game_choice:
            print(f"You played {game_choice} with {self.adadachi.name}, and that is their \
favorite game! They LOVED IT!")
            self.adadachi.favorite_increase_happiness()
        else:
            print(f"You played {game_choice} with {self.adadachi.name}!")
            self.adadachi.increase_happiness()
            

    def feed(self):
        player_food_choice = input(f'''
**************************************************
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^                                                ^
              What would you like           
^                  to feed                       ^
                  {self.adadachi.name}?:            
^                 ============                   ^
         "A" for {self.inventory['foods'][0]}                               
^                                                ^
         "B" for {self.inventory['foods'][1]}  
^                                                ^
         "C" for {self.inventory['foods'][2]}    
^                                                ^
         "D" for {self.inventory['foods'][3]}                                                
**************************************************
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''')
        while player_food_choice:
                if player_food_choice.lower() == "a":
                    food_choice = self.inventory['foods'][0]
                    self.food_result(food_choice)
                    break
                elif player_food_choice.lower() == "b":
                    food_choice = self.inventory['foods'][1]
                    self.food_result(food_choice)
                    break
                elif player_food_choice.lower() == "c":
                    food_choice = self.inventory['foods'][2]
                    self.food_result(food_choice)
                    break
                elif player_food_choice.lower() == "d":
                    food_choice = self.inventory['foods'][3]
                    self.food_result(food_choice)
                    break
                else:
                    player_food_choice = input("Please make a valid selection:  ")


    def food_result(self, food_choice):
        adadachi_hates = self.inventory['foods'][self.adadachi.personality["hates_food"]]
        adadachi_fav = self.inventory['foods'][self.adadachi.personality["fav_food"]]
        if adadachi_hates == food_choice:
            print(f"You fed {food_choice} to {self.adadachi.name} but that is \
their least favorite food! Whomp Whomp!")
            self.adadachi.decrease_happiness()
        elif adadachi_fav == food_choice:
            print(f"You fed {food_choice} to {self.adadachi.name}, and that is their \
favorite food! They LOVED IT!")
            self.adadachi.favorite_increase_happiness()
        else:
            print(f"You fed {food_choice} to {self.adadachi.name}!")
            self.adadachi.increase_happiness()
        