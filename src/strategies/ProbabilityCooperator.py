from src.Game import Game
from src.strategies.Strategy import Strategy
from random import choices


class ProbabilityCooperator(Strategy):
    def __init__(self, player_number: int, prob_coop=0.5) -> None:
        super().__init__(player_number)
        self.prob_coop = prob_coop

    def play(self, game: Game):
        options = ["C", "D"]
        res = choices(options, [self.prob_coop, 1 - self.prob_coop])[0]
        return res
