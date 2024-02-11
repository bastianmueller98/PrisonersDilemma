import unittest
from src.Game import Game


class MyTestCase(unittest.TestCase):
    def test_game_init(self):
        g = Game("player1", "player2", "C", "C")
        self.assertEqual(g.player1, "player1")
        self.assertEqual(g.player2, "player2")
        self.assertEqual(g.history[0].player1_move, "C")
        self.assertEqual(g.history[0].player2_move, "C")

    def test_game_init_with_moves(self):
        g = Game("player1", "player2", "D", "C")
        self.assertEqual(g.player1, "player1")
        self.assertEqual(g.player2, "player2")
        self.assertEqual(g.history[0].player1_move, "D")
        self.assertEqual(g.history[0].player2_move, "C")

    def test_game_init_with_random_moves(self):
        g = Game("player1", "player2")
        self.assertEqual(g.player1, "player1")
        self.assertEqual(g.player2, "player2")
        self.assertIn(g.history[0].player1_move, ["C", "D"])
        self.assertIn(g.history[0].player2_move, ["C", "D"])

    def test_game_payoffs(self):
        g = Game("player1", "player2", "C", "D")
        self.assertEqual(g.payoffs[("C", "C")], (3, 3))
        self.assertEqual(g.payoffs[("C", "D")], (0, 5))
        self.assertEqual(g.payoffs[("D", "C")], (5, 0))
        self.assertEqual(g.payoffs[("D", "D")], (1, 1))

    def test_game_payoff_matrix_names(self):
        g = Game("player1", "player2", "C", "C")
        self.assertEqual(g.player1_payoff_matrix_names[("C", "C")], "R")
        self.assertEqual(g.player1_payoff_matrix_names[("C", "D")], "S")
        self.assertEqual(g.player1_payoff_matrix_names[("D", "C")], "T")
        self.assertEqual(g.player1_payoff_matrix_names[("D", "D")], "P")
        self.assertEqual(g.player2_payoff_matrix_names[("C", "C")], "R")
        self.assertEqual(g.player2_payoff_matrix_names[("C", "D")], "T")
        self.assertEqual(g.player2_payoff_matrix_names[("D", "C")], "S")
        self.assertEqual(g.player2_payoff_matrix_names[("D", "D")], "P")


if __name__ == "__main__":
    unittest.main()
