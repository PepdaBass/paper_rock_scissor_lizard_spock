from player import Player
import random



class Artificial_Intelligence(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self, name):
        self.name = 'Skynet'

    def choose_gesture(self):
        self.random_index = random.randrange(0, 4)
        return self.gesture_list[self.random_index]

        

        
        
       