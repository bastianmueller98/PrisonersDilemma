from Game import Game
from strategies.Strategy import Strategy


class TitForTatStrategy(Strategy):
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)

    def play(self, game: Game):
        if self.player_number == 1:
            last_opponent_move = game.history[-1].player2_move
        else:
            last_opponent_move = game.history[-1].player1_move
        return last_opponent_move
