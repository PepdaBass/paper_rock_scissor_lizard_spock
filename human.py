from player import Player


class Human(Player):
    def __init__(self): # <-- Not sure if we need to use a name argument if we are going to have the user enter their name.
        super().__init__()
        # self.name = input('Please enter your name: ')
        # self.choose_name()
    
    def choose_name(self):
        self.name = input('Please enter your name: ')
        print(self.name)

    def choose_gesture(self):
        print('Choose your gesture:')
        gesture_option = ('Enter 1 for Rock\n',
              'Enter 2 for Paper\n',
              'Enter 3 for Scissors\n',
              'Enter 4 for Lizard\n',
              'Enter 5 for Spock\n')
        user_choice = input(gesture_option)
        print(user_choice)
        return int(user_choice) - 1 