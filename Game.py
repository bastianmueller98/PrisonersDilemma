from GameState import GameState


class Game:
    def __init__(self, player1_move, player2_move):
        self.payoffs = {
            ("C", "C"): (3, 3),
            ("C", "D"): (0, 5),
            ("D", "C"): (5, 0),
            ("D", "D"): (1, 1)
        }
        self.history = []
        self.play(player1_move, player2_move)
        self.player1_total_payoff = 0
        self.player2_total_payoff = 0


    def get_initial_state(self):
        return GameState(0, ("", ""), (0, 0))

    def play(self, move1, move2):
        gs = GameState(len(self.history) + 1, (move1, move2), self.payoffs[(move1, move2)])
        self.history.append(gs)
        self.player1_total_payoff = sum([x.payoffs[0] for x in self.history])
        self.player2_total_payoff = sum([x.payoffs[1] for x in self.history])
        return gs
    
    def end_game(self):
        return f"""End result after {len(self.history)} rounds:
Player 1 total payoff: {self.player1_total_payoff}
Player 1 avg. payoff: {self.player1_total_payoff/len(self.history)}
Player 2 total payoff: {self.player2_total_payoff}
Player 2 avg. payoff: {self.player2_total_payoff/len(self.history)}."""
