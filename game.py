from human import Human
from artificial_intelligence import Artificial_Intelligence
from player import Player
import time 

class Game:
    def __init__(self):
        self.player_one = Human('John')
        self.player_two = Human('Sara')
        self.player_three = Artificial_Intelligence()
        # self.player_vessel = Player() # Not sure what's going on with gesture_list from Player. Can't
        #                               # get it to be recognized.

    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.

    def display_greeting(self):
        print('Welcome to Dueling Gestures')
        print('Do you need to settle a score. Are you confident you can take on skynet.')
        print('This is the place for you.')
        print('The game is Rock, Paper, Scissors, Lizard, Spock.')
        print('The game is a best of 3')
        print('The rules work like this.')
        


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
        self.player_wins = 0
        self.artificial_intelligence_wins = 0
        self.games_played = 0
        while self.artificial_intelligence_wins < 2 or self.player_wins < 2):
            self.game_rules_method()
            print(self.games_played)

            


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
            self.player_wins = self.player_wins + 1
        elif self.player_one.choose_gesture() == 0 and (self.player_three.choose_gesture() == 2 or self.player_three.choose_gesture() == 3):
            print(f'{self.player_one.name} wins with {self.gesture_list[0]} !')# <-- gesture_list not working. need workaround
            self.player_wins = self.player_wins + 1 
        elif self.player_one.choose_gesture() == 1 and (self.player_three.choose_gesture() == 0 or self.player_three.choose_gesture() == 4):
            print('Player one wins!')
            self.player_wins = self.player_wins + 1
        elif self.player_one.choose_gesture() == 2 and (self.player_three.choose_gesture() == 1 or self.player_three.choose_gesture() == 3):
            print('Player one wins!')
            self.player_wins = self.player_wins + 1
        elif self.player_one.choose_gesture() == 3 and (self.player_three.choose_gesture() == 4 or self.player_three.choose_gesture() == 1):
            print('Player one wins!')
            self.player_wins = self.player_wins + 1
        elif self.player_one.choose_gesture() == 4 and (self.player_three.choose_gesture() == 0 or self.player_three.choose_gesture() == 2):
            print('Player one wins!')
            self.player_wins = self.player_wins + 1
        else:
            print('Player two wins!')
            self.artificial_intelligence_wins = self.artificial_intelligence_wins + 1
    def round(self):
        pass

    def results_record(self):
        pass

    def display_winner(self):
        pass