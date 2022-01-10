from human import Human
from artificial_intelligence import Artificial_Intelligence
from player import Player # <-- No need to import Player class


class Game:
    def __init__(self):
        # self.player_blueprint = Player()
        self.player_one = Human()
        self.player_two = Human()
        self.player_three = Artificial_Intelligence()
        
        # self.player_vessel = Player() # Not sure what's going on with gesture_list from Player. Can't
        #                               # get it to be recognized.

    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.initiate_one_player_game()
        # print(self.player_one.gesture_list[0])
        # self.player_one.choose_name()
  

    def display_greeting(self):
        print('Welcome to Dueling Gestures')
        print('Do you need to settle a score. Are you confident you can take on skynet?')
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
        # self.player_wins = 0                  <-- self.player_one.score already equals zero
        # self.artificial_intelligence_wins = 0 <-- self.player_three.score same thing
        self.player_one.choose_name()
        self.games_played = 0
        while self.player_three.score < 2 or self.player_one.score < 2: #Can't get the game to step into this while loop???
            self.player_one_choice = self.player_one.choose_gesture()
            #print(self.player_one.choose_gesture())
            self.player_three_choice = self.player_three.choose_gesture()
            self.game_rules_method()
            #print(self.player_three.choose_gesture())
            self.games_played += self.games_played + 1
            print(self.games_played)
        # game_complete = False
        # while game_complete is False:
        #     if self.player_three.score < 2 or self.player_one.score < 2: #Can't get the game to step into this while loop???
        #         self.game_rules_method() 
        #         self.player_one.choose_gesture()
        #         print(self.player_one.choose_gesture())
        #         self.player_three.choose_gesture()
        #         print(self.player_three.choose_gesture())
        #         print(self.games_played)
        #     else:
        #         game_complete = True
          

            


    def initiate_two_player_game(self):
        pass
    
    
    # 0 is Rock
    # 1 is Paper
    # 2 is Scissors
    # 3 is Lizard
    # 4 is Spock
    def game_rules_method(self):
        # one_round = False
        # while one_round is False:
        if self.player_one_choice == self.player_three_choice:
            print('It is a tie!')
        elif self.player_one_choice == 0 and (self.player_three_choice == 2 or self.player_three_choice == 3):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[0]} !')# <-- gesture_list not working. need workaround
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 1 and (self.player_three_choice == 0 or self.player_three_choice == 4):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[1]} !')
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 2 and (self.player_three_choice == 1 or self.player_three_choice == 3):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[2]} !')
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 3 and (self.player_three_choice == 4 or self.player_three_choice == 1):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[3]} !')
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 4 and (self.player_three_choice == 0 or self.player_three_choice == 2):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[4]} !')
            self.player_one.score = self.player_one.score + 1 
        else:
            print('Player two wins!')
            self.player_three.score = self.player_three.score + 1
    def round(self):
        pass

    def results_record(self):
        pass

    def display_winner(self):
        pass