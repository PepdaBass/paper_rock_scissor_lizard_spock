from player import Player
import random



class Artificial_Intelligence(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self, name):
        self.name = 'Skynet'

    def choose_gesture(self):
        computer_choice = self.gesture_list[random.randomint(0, 4)]
        return int(computer_choice)

        

        
        
       