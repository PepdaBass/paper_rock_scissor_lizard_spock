from player import Player
import random



class Artificial_Intelligence(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Skynet'

    def choose_name(self, name): # <-- Do we need a 'choose_name' function if we only have one name for the A.I.?
        self.name = 'Skynet'

    def choose_gesture(self):
        # computer_choice = self.gesture_list[random.randint(0, 4)] #<-- computer_choice is coming back as a string
        computer_choice = random.randint(0, 4)
        print(computer_choice)
        return computer_choice

        

        
        
       