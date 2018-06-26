""" Rock Paper Scissors
1-Rock beats scissors
2-Scissors beat paper
3-paper beats rock
Creating a Player vs. Computer Version"""
import random

class RPS:
    scorePlayer = 0
    scoreComputer = 0
    flag = 0
    def __init__(self, number_Wins):
        self.number_Wins = number_Wins
        """ Specify number of wins needed to win a RPS Game """

    def StartGame(self):
        self.Possible_choices = ['R', 'P', 'S']

        while self.flag != 1:
            self.move_player = str(input('Enter a Move (R, P, S): '))
            self.Choice = random.choice(self.Possible_choices)

            if self.Choice == self.move_player:
                print('Draw. You both selected', self.Choice)

            elif self.Choice == 'R' and self.move_player == 'S':
                self.scoreComputer += 1

            elif self.Choice == 'R' and self.move_player == 'P':
                self.scorePlayer += 1

            elif self.Choice == 'P' and self.move_player == 'S':
                self.scorePlayer += 1

            elif self.Choice == 'P' and self.move_player == 'R':
                self.scoreComputer += 1

            elif self.Choice == 'S' and self.move_player == 'R':
                self.scorePlayer += 1

            elif self.Choice == 'S' and self.move_player == 'P':
                self.scoreComputer += 1
            self.flag = RPS.CheckWhoWon(self)

    def CheckWhoWon(self):

        if self.scorePlayer == self.number_Wins:
            print('Congratuations! You won.')
            return 1

        elif self.scoreComputer == self.number_Wins:
            print('The computer won. ')
            return 1

        else:
            print('The score is:\nPlayer:', self.scorePlayer, 'vs. Computer:', self.scoreComputer)


game_one = RPS(3)
game_one.StartGame()


