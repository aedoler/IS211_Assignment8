#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import random
import sys

"""player1type = raw_input("Is Player 1 a 'human' or a 'computer'?").lower()
player2type = raw_input("Is Player 2 a 'human' or a 'computer'?").lower()"""




class Dice:
    """Class simulates dice"""

    def __init__(self):
        self.diceValue = random.randint(1, 6)

    def roll(self):
        """Simulates dice roll"""
        return self.diceValue

class TurnScoreKeeper:
    """Keeps temp round score for player"""

    def __init__(self):
        self.value = 0

    def addTurnScore(self, dieValue):
        """Adds score for round to player' total score"""
        self.value += dieValue

    def resetScore(self):
        """Resets round score after each turn"""
        self.value = 0


class Player:
    """Class that simulates a player"""

    def __init__(self):
        self.playerName = None
        self.turnScore = 0
        self.currentScore = 0
        self.input = None

    def addTurnScore(self, dieValue):
        """Adds score for round to player' total score"""
        self.turnScore += dieValue

    def resetTurnScore(self):
        """Resets round score after each turn"""
        self.turnScore = 0


    def addScore(self, points):
        """Adds points to player's total score"""
        self.currentScore += points

    def newGameReset(self):
        """Resets players' scores if a new game is started"""
        self.currentScore = 0

    def stats(self):
        """Returns player's name and current score"""
        return "{} has a current core of {} \n\n".format(self.name, self.currentScore)

    def rollOrHold(self):
        """Returns option to either hold score or re-roll"""
        self.input = raw_input('Would you like hold your score or re-roll? Type "h" '
                                'to hold or "r" to re-roll.')

class HumanPlayer(Player):
    def __init__(self):
        self.name = None
        Player.__init__(self)

class ComputerPlayer(Player):
    def __init__(self):
        self.name = None
        Player.__init__(self)

        hold1 = 25
        hold2 = 100 - self.currentScore
        if hold1 < hold2:
            hold_score = hold1
        else:
            hold_score = hold2

        if self.turnScore < hold_score:
            self.input = 'r'
        elif self.turnScore >= hold_score:
            self.input = 'h'





class PlayerFactory(Player):

    def getPlayers(self, player):
        if player == 'human':
            return HumanPlayer()
        if player == 'computer':
            return ComputerPlayer()


class GameState:
    """Class simulates gameplay"""

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.p1.name = 'Player 1'
        self.p2.name = 'Player 2'




    def gamePlay(self):
        """Gameplay"""
        while self.p1.currentScore < 100 and self.p2.currentScore < 100:
            for player in (self.p1, self.p2):


                print "It's {}'s turn.".format(player.name)
                print 'Rolling die............. \n'
                while True:

                    diceValue = Dice()
                    diceValue = diceValue.roll()

                    if diceValue == 1:
                        print "You have rolled a 1. You score no points this round. Next Player's turn. \n"
                        player.resetTurnScore()
                        break

                    player.addTurnScore(diceValue)

                    print "You rolled a {}. Your total round score is {}".format(diceValue, player.turnScore)
                    player.rollOrHold()
                    if player.input == 'h':
                        player.addScore(player.turnScore)
                        print player.stats()
                        player.resetTurnScore()
                        break

                if player.currentScore >= 100:
                    print '{} has won this game! \n'.format(player.name)
                    newGame = raw_input('Would you like to start a new game? Type "y" or "n". ')
                    if newGame == 'y':
                        self.p1.newGameReset()
                        self.p2.newGameReset()
                        continue
                    else:
                        print "Bye!"
                        sys.exit()



if __name__ == "__main__":
    playerFactory = PlayerFactory()
    player1type = 'human'
    player2type = 'computer'
    player1 = playerFactory.getPlayers(player1type)
    player2 = playerFactory.getPlayers(player2type)
    game = GameState(player1, player2)
    game.gamePlay()