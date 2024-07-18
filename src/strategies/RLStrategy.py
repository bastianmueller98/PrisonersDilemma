from src.Game import Game
from src.strategies.Strategy import Strategy
from random import choices


class RLStrategy(Strategy):
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)

    def play(self, game: Game):
        return "C"
