#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import random
import sys
import time
import signal

player1type = raw_input("Is Player 1 a 'human' or a 'computer'? ").lower()
player2type = raw_input("Is Player 2 a 'human' or a 'computer'? ").lower()
timedGameInput = raw_input("Timed game? 'Yes' or 'No' ").lower()



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

    def rollOrHold(self):
        """Returns option to either hold score or re-roll"""
        print 'IN COMPUTER CLASS'  #Check to make sure this method is called
        print 'The computer is thinking........'
        time.sleep(2)

        hold25 = 25
        hold100 = 100 - self.currentScore
        if hold25 < hold100:
            hold_score = hold25
        else:
            hold_score = hold100

        if self.turnScore < hold_score:
            self.input = 'r'
        elif self.turnScore >= hold_score:
            self.input = 'h'


class PlayerFactory:

    def __init__(self, player):
        if player == 'human':
            self.getplayer = HumanPlayer()
        if player == 'computer':
            self.getplayer =  ComputerPlayer()


class Game:
    """Class simulates gameplay"""

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        print self.p1  # check what kind of player is being created
        print self.p2
        self.p1.name = 'Player 1'
        self.p2.name = 'Player 2'
        self.startTime = time.time()

    def hookTimedGame(self):

        print "in game class" # testing


    def gamePlay(self):
        """Gameplay"""
        while self.p1.currentScore < 100 and self.p2.currentScore < 100:
            for player in (self.p1, self.p2):

                if timedGameInput == 'yes':  # Check to see if time has passed the limit
                    currentTime = time.time()
                    if currentTime - self.startTime > 10:
                        print "Time up!"
                        if self.p1.currentScore > self.p2.currentScore:
                            print "Player 1 is the winner!"
                        elif self.p2.currentScore > self.p1.currentScore:
                            print "Player 2 is the winner!"
                        else:
                            print "It' a tie!"
                        sys.exit()

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
                    elif player.input == 'r':
                        continue

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



class TimedGameProxy(Game):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.timedGame = Game(self.player1, self.player2)


    def timedGameMethod(self):
        self.timedGame.gamePlay()







if __name__ == "__main__":
    if timedGameInput == "no":
        player1 = PlayerFactory(player1type)
        player2 = PlayerFactory(player2type)
        game = Game(player1.getplayer, player2.getplayer)
        game.gamePlay()
    elif timedGameInput == "yes":

        player1 = PlayerFactory(player1type)
        player2 = PlayerFactory(player2type)
        game = TimedGameProxy(player1.getplayer, player2.getplayer)
        game = game.timedGameMethod()