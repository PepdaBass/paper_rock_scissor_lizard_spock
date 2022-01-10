from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self):
        self.name = input('Please enter your name: ')
        
    def choose_gesture(self):
        print('Choose your gesture:')
        gesture_option = ('Enter 1 for Rock\n'
                            'Enter 2 for Paper\n'
                            'Enter 3 for Scissors\n'
                            'Enter 4 for Lizard\n'
                            'Enter 5 for Spock\n')
        user_choice = input(gesture_option)
        valid_choice = False
        while valid_choice == False:
            if user_choice not in ['1', '2', '3', '4', '5']:
                print('That is not one of the options. Try again')
                user_choice = input(gesture_option)
            else:
                valid_choice = True
                return int(user_choice) - 1