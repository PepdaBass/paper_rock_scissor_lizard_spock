from human import Human
from artificial_intelligence import Artificial_Intelligence
from player import Player

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human()
        self.player_three = Artificial_Intelligence()
        # self.player_vessel = Player() # Not sure what's going on with gesture_list from Player. Can't
        #                               # get it to be recognized.

    def run_game(self):
        pass

    def display_greeting(self):
        pass
        # Dueling Gestures

    def display_rules(self):
        print('''
        Rock crushes Scissors 
        Scissors cuts Paper 
        Paper covers Rock 
        Rock crushes Lizard
        Lizard poisons Spock  
        Spock smashes Scissors 
        Scissors decapitates Lizard 
        Lizard eats Paper 
        Paper disproves Spock 
        Spock vaporizes Rock
        ''')

    def initiate_one_player_game(self):
        pass

    def initiate_two_player_game(self):
        pass
    
    
    # 0 is Rock
    # 1 is Paper
    # 2 is Scissors
    # 3 is Lizard
    # 4 is Spock
    def game_rules_method(self):
        if self.player_one.choose_gesture() == self.player_three.choose_gesture():
            print('It is a tie!')
        elif self.player_one.choose_gesture() == 0 and (self.player_three.choose_gesture() == 2 or self.player_three.choose_gesture() == 3):
            print(f'{self.player_one.name} wins with {self.gesture_list[0]} !') # <-- gesture_list not working. need workaround
        elif self.player_one.choose_gesture() == 1 and (self.player_three.choose_gesture() == 0 or self.player_three.choose_gesture() == 4):
            print('Player one wins!')
        elif self.player_one.choose_gesture() == 2 and (self.player_three.choose_gesture() == 1 or self.player_three.choose_gesture() == 3):
            print('Player one wins!')
        elif self.player_one.choose_gesture() == 3 and (self.player_three.choose_gesture() == 4 or self.player_three.choose_gesture() == 1):
            print('Player one wins!')
        elif self.player_one.choose_gesture() == 4 and (self.player_three.choose_gesture() == 0 or self.player_three.choose_gesture() == 2):
            print('Player one wins!')
        else:
            print('Player two wins!')
    def round(self):
        pass

    def results_record(self):
        pass

    def display_winner(self):
        pass