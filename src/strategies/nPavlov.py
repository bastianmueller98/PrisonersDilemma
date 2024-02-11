from src.Game import Game
from src.strategies.Strategy import Strategy
from random import choices


class nPavlov(Strategy):
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)
        self.prob_coop = 1

    def play(self, game: Game):
        if self.player_number == 1:
            last_payoff_name = game.player1_payoff_matrix_names[
                game.history[-1].player1_move, game.history[-1].player2_move
            ]
        else:
            last_payoff_name = game.player2_payoff_matrix_names[
                game.history[-1].player1_move, game.history[-1].player2_move
            ]
        to_add = self.probs_to_add(last_payoff_name, len(game.history))
        self.prob_coop += to_add
        self.prob_coop = max(0, min(1, self.prob_coop))
        return choices(["C", "D"], [self.prob_coop, 1 - self.prob_coop])[0]

    def probs_to_add(self, payoff_name, n):
        if payoff_name == "R":
            return 1 / n
        elif payoff_name == "P":
            return -1 / n
        elif payoff_name == "T":
            return 2 / n
        elif payoff_name == "S":
            return -2 / n
        else:
            return 0
