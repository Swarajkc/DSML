"""creating a code to simulate a game of rock paper scissors.
to simulate:
- human vs human
- human vs pc
"""
import random
class RockPaperScissors():
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
    
    def get_human_choice(self):
        choice = input("Enter rock, paper, or scissors: ").lower()
        while choice not in self.choices:
            print("Invalid choice. Try again.")
            choice = input("Enter rock, paper, or scissors: ").lower()
        return choice

    def get_computer_choice(self):
        return random.choice(self.choices)
            
    def play_game(self, mode):
        if mode == 'hvh':
            player1 = self.get_human_choice()
            player2 = self.get_human_choice()
        else: 
            player1 = self.get_human_choice()
            player2 = self.get_computer_choice()
            print(f"Computer chose: {player2}")
        
        if player1==player2:
            result = "it is a tie"
        elif (player1 == 'rock' and player2 == 'scissors') or \
             (player1 == 'scissors' and player2 == 'paper') or \
             (player1 == 'paper' and player2 == 'rock'):
            result = "Player 1 wins!"
        else:
            result = "Player 2 wins!"

        print(result)
        
game = RockPaperScissors()
mode = input("Choose mode - Human vs Human (hvh) or Human vs PC (hvp): ")
game.play_game(mode)