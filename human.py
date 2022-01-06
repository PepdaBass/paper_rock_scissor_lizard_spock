from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
    
    def choose_name(self, name):
        self.name = input('Please enter your name: ')