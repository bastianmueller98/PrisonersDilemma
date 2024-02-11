from GameState import GameState
from random import choice
import matplotlib.pyplot as plt


class Game:
    def __init__(
        self,
        player1,
        player2,
        player1_move=None,
        player2_move=None,
        payoffs={
            ("C", "C"): (3, 3),
            ("C", "D"): (0, 5),
            ("D", "C"): (5, 0),
            ("D", "D"): (1, 1),
        },
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.payoffs = payoffs
        self.history = []
        if player1_move is None or player2_move is None:
            player1_move, player2_move = self.random_first_moves()
        self.play(player1_move, player2_move)
        self.player1_total_payoff = 0
        self.player2_total_payoff = 0
        self.player1_payoff_matrix_names = {
            ("C", "C"): "R",
            ("C", "D"): "S",
            ("D", "C"): "T",
            ("D", "D"): "P",
        }
        self.player2_payoff_matrix_names = {
            ("C", "C"): "R",
            ("C", "D"): "T",
            ("D", "C"): "S",
            ("D", "D"): "P",
        }

    @classmethod
    def random_first_moves(cls):
        choices = ["C", "D"]
        return choice(choices), choice(choices)

    def get_initial_state(self):
        return GameState(0, ("", ""), (0, 0))

    def play(self, move1, move2):
        gs = GameState(
            len(self.history) + 1,
            (move1, move2),
            self.payoffs[(move1, move2)],
        )
        self.history.append(gs)
        gs.player1_total_payoff = sum([x.payoffs[0] for x in self.history]) / len(
            self.history
        )
        gs.player2_total_payoff = sum([x.payoffs[1] for x in self.history]) / len(
            self.history
        )
        self.history[-1] = gs
        return gs

    def end_game(self, plot_results=False, average_lines=False):
        if plot_results:
            player1_payoffs = [x.player1_total_payoff for x in self.history]
            player2_payoffs = [x.player2_total_payoff for x in self.history]
            rounds = list(range(1, len(self.history) + 1))

            plt.plot(
                rounds,
                player1_payoffs,
                label=f"Player 1: {self.player1.__class__.__name__}",
                color="blue",
            )
            plt.plot(
                rounds,
                player2_payoffs,
                label=f"Player 2: {self.player2.__class__.__name__}",
                color="orange",
            )
            if average_lines:
                player1_cum_mov_avg_payoff = [
                    sum(player1_payoffs[:i]) / i
                    for i in range(1, len(self.history) + 1)
                ]
                plt.plot(
                    rounds,
                    player1_cum_mov_avg_payoff,
                    label="Cumulative moving average P1",
                    color="green",
                    linestyle="--",
                )
                player2_cum_mov_avg_payoff = [
                    sum(player2_payoffs[:i]) / i
                    for i in range(1, len(self.history) + 1)
                ]
                plt.plot(
                    rounds,
                    player2_cum_mov_avg_payoff,
                    label="Cumulative moving average P2",
                    color="red",
                    linestyle="--",
                )

            plt.title("Prisoners Dilemma average payoffs")
            plt.xlabel("Rounds")
            plt.ylabel("Avg. Payoff")
            plt.legend()
            plt.show()

        return f"""End result after {len(self.history)} rounds:
    Player 1 total payoff: {self.player1_total_payoff}
    Player 1 avg. payoff: {self.player1_total_payoff/len(self.history)}
    Player 2 total payoff: {self.player2_total_payoff}
    Player 2 avg. payoff: {self.player2_total_payoff/len(self.history)}."""
