from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
    
    def choose_name(self, name):
        self.name = input('Please enter your name: ')
        print(self.name)

    def choose_gesture(self):
        print('Choose your gesture:')
        gesture_option =('Enter 1 for Rock\n',
              'Enteer 2 for Paper\n',
              'Enter 3 for Scissors\n',
              'Enter 4 for Lizard\n',
              'Enter 5 for Spock\n')
        user_choice = input(gesture_option)
        return int(user_choice) - 1 