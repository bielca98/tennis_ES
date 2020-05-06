# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:20:01 2020

@author: Biel Castaño, Agustín Martínez, Alex Moro
"""

from src.main.playingState import PlayingState
from src.main.Player import Player


class Game:
    def __init__(self, first: Player, second: Player):
        self.player1 = first
        self.player2 = second
        self.gameState = PlayingState()

    def won_point(self, winner: Player):
        if winner.get_name() == "player1":
            self.player1.add_point()
        else:
            self.player2.add_point()
        self.gameState.change_state(self.player1.get_points(), self.player2.get_points())

    def get_score(self) -> str:
        return self.gameState.get_state()
