from random import randint
from Player import Player

class ManualPlayer(Player):

    # select one column
    def move(self, player_code, board):
        g = input("Enter a column (0..6) : ") 
        return int(g)
