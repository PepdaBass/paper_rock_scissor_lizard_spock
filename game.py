from human import Human
from artificial_intelligence import Artificial_Intelligence
import time


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human()
        self.player_three = Artificial_Intelligence()
        
      

    def run_game(self):
        # self.display_greeting()
        # self.display_rules()
        self.choose_opponent()
        self.display_winner()

    def display_greeting(self):
        print('Welcome to Dueling Gestures')
        time.sleep(1)
        print('Do you need to settle a score. Are you confident you can take on skynet?')
        time.sleep(1)
        print('This is the place for you.')
        time.sleep(1)
        print('The game is Rock, Paper, Scissors, Lizard, Spock.')
        time.sleep(1)
        print('The game is a best of 3')
        time.sleep(1)
        print('The rules work like this.')
        time.sleep(1)
        


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
        time.sleep(3)

    
    def choose_opponent(self):
        self.player_opponent = int(input('Would you like to play sing player or multiplayer: Press 1 for single player game. Press 2 for multiplayer game.'))
        choose_game = False
        while choose_game == False:
            if self.player_opponent != 1 and self.player_opponent != 2:
               self.player_opponent = int(input('Not a valid choice. Please select again. Pease select 1 or 2'))
            elif self.player_opponent == 1:
                self.initiate_one_player_game()
                choose_game = True
            elif self.player_opponent == 2:
                self.initiate_two_player_game()
                choose_game = True
            
                  
    
    
    def initiate_one_player_game(self):
        self.player_one.choose_name()
        print(f'{self.player_one.name} goes first.')
        time.sleep(1)
        self.games_played = 0
        self.opponent = self.player_three
        while self.player_three.score < 2 and self.player_one.score < 2: #Can't get the game to step into this while loop???
            self.player_one_choice = self.player_one.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.gesture_list[self.player_one_choice]}')
            time.sleep(1)
            #print(self.player_one.choose_gesture())
            self.opponent_choice = self.player_three.choose_gesture()
            print(f'{self.opponent.name} chose {self.opponent.gesture_list[self.opponent_choice]}')
            time.sleep(1)
            self.game_rules_method()
            #print(self.player_three.choose_gesture())
            self.games_played += 1
            print(f'You have played {self.games_played} games.')
        
          

            


    def initiate_two_player_game(self):
        self.player_one.choose_name()
        self.player_two.choose_name()
        self.games_played = 0
        self.opponent = self.player_two
        print(f'{self.player_one.name} goes first.')
        while self.opponent.score < 2 and self.player_one.score < 2: #Can't get the game to step into this while loop???
            self.player_one_choice = self.player_one.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.gesture_list[self.player_one_choice]}')
            #print(self.player_one.choose_gesture())
            self.opponent_choice = self.opponent.choose_gesture()
            print(f'{self.opponent.name} chose {self.opponent.gesture_list[self.opponent_choice]}')
            self.game_rules_method()
            #print(self.player_three.choose_gesture())
            self.games_played += 1
            print(f'You have played {self.games_played} games.')
    
    
    # 0 is Rock
    # 1 is Paper
    # 2 is Scissors
    # 3 is Lizard
    # 4 is Spock
    def game_rules_method(self):
        if self.player_one_choice == self.opponent_choice:
            print('It is a tie!')
        elif self.player_one_choice == 0 and (self.opponent_choice == 2 or self.opponent_choice == 3):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[0]} !')# <-- gesture_list not working. need workaround
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 1 and (self.opponent_choice == 0 or self.opponent_choice == 4):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[1]} !')
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 2 and (self.opponent_choice == 1 or self.opponent_choice == 3):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[2]} !')
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 3 and (self.opponent_choice == 4 or self.opponent_choice == 1):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[3]} !')
            self.player_one.score = self.player_one.score + 1 
        elif self.player_one_choice == 4 and (self.opponent_choice == 0 or self.opponent_choice == 2):
            print(f'{self.player_one.name} wins with {self.player_one.gesture_list[4]} !')
            self.player_one.score = self.player_one.score + 1 
        else:
            print(f'{self.opponent.name} wins with {self.opponent.gesture_list[self.opponent_choice]}!')
            self.opponent.score = self.opponent.score + 1
    def round(self):
        pass

    def results_record(self):
        pass

    def display_winner(self):
        if self.player_opponent == 1:
            if self. player_one.score == 2:
                print(f'{self.player_one.name} is the winner. You have saved mankind.')
            else:
                print(f'{self.opponent.name} is the winner. Skynet has taken over.')
        elif self.player_opponent == 2:
            if self.player_one.score == 2:
                print(f'{self.player_one.name} is the winner.')
            else:
                print(f'{self.opponent.name} is the winner.')