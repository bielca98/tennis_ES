# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:23:03 2020

@author: Biel Castaño, Agustín Martínez, Alex Moro
"""


class PlayingState:

    def __init__(self):
        self.state = "Love-All"
        self.mode = "No-Deuce"

    def get_state(self) -> str:
        return self.state

    def get_state_mode(self) -> str:
        return self.mode

    def change_state(self,points_player1, points_player2) -> None:
        #       FIRST OF ALL DRAWS
        if points_player1 == points_player2:
            if points_player1 == 0:
                self.state = "Love-All"           
            elif points_player1 == 1:
                self.state = "Fifteen-All"            
            elif points_player1 == 2:
                self.state = "Thirty-All"
            else:
                self.state = "Deuce"
        elif points_player1 < 4 and points_player2 < 4: #NOT WINNER
            if points_player1 == 0:
                score_1 = "Love"
            elif points_player1 == 1:
                score_1 = "Fifteen"
            elif points_player1 == 2:
                score_1 = "Thirty"
            elif points_player1 == 3:
                score_1 = "Forty" 
            if points_player2 == 0:
                score_2 = "Love"
            elif points_player2 == 1:
                score_2 = "Fifteen"
            elif points_player2 == 2:
                score_2 = "Thirty"
            elif points_player2 == 3:
                score_2 = "Forty" 
            if points_player2 < 4 and points_player1 < 4:                     
                self.state = "{}-{}".format(score_1, score_2)
        else:   #WINNER AND ADVANTAGE SITUATION
            if (points_player1 - points_player2) > 1:
                self.state = "Win for player1"
            elif (points_player1 - points_player2) < -1:
                self.state = "Win for player2"
            elif points_player1 > points_player2:
                self.state = "Advantage player1"
            else :
                self.state = "Advantage player2"
        
        
       