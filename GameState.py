class GameState:
    def __init__(self, round, moves, payoffs) -> None:
        self.player1_move = moves[0]
        self.player2_move = moves[1]
        self.round = round
        self.payoffs = payoffs
