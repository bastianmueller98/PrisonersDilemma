from Strategy import Strategy
from Game import Game


class AlwaysDefectStrategy(Strategy):
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)
        
    def play(self, game: Game):
        return "D"
