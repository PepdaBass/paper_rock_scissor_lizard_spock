from player import Player
import random



class Artificial_Intelligence(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Skynet'

    def choose_gesture(self):
        computer_choice = random.randint(0, 4)
        return computer_choice

        

        
        
       