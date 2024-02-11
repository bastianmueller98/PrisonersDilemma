from Game import Game
from strategies.Strategy import Strategy


class TFTTStrategy(Strategy):
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)

    def play(self, game: Game):
        if len(game.history) < 2:
            return "C"

        last_opponent_move = (
            game.history[-1].player2_move
            if self.player_number == 1
            else game.history[-1].player1_move
        )
        second_to_last_opponent_move = (
            game.history[-2].player2_move
            if self.player_number == 1
            else game.history[-2].player1_move
        )

        if last_opponent_move == "D" and second_to_last_opponent_move == "D":
            return "D"
        return "C"
