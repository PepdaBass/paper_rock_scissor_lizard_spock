from player import Player



class Artificial_Intelligence(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self, name):
        self.name = 'Skynet'