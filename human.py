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
        user_choice = int(input(gesture_option))
        valid_choice = False
        while valid_choice == False:
            if user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4 and user_choice != 5:
                print('That is not one of the options. Try again')
                user_choice = int(input(gesture_option))
            else:
                valid_choice = True
                return int(user_choice) - 1 
        
        
        
        # valid_choice = False
        # while valid_choice == False:
        #     if user_choice != range(5):
        #         print('That is not one of the options. Try again')
        #         user_choice = int(input(gesture_option))
        #     elif user_choice == range(5):
        #         valid_choice = True
        #         return user_choice - 1 