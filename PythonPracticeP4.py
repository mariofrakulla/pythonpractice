""" Guessing Game
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""
import random

class guessGame:
    listChoice = [1,2,3,4,5,6,7,8,9]
    def __init__(self):
        self.randomNum = random.choice(self.listChoice)

    def StartGame(self):
        self.Player = int(input('Enter a number: '))
        while self.Player != self.randomNum:

            if self.Player < self.randomNum:
                print('Choose Higher')
                self.Player = int(input('Enter a number: '))

            elif self.Player > self.randomNum:
                print('Choose Lower')
                self.Player = int(input('Enter a number: '))

        print('Congrats! You won.')

game_one = guessGame()
game_one.StartGame()
