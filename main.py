from Game import Game
from strategies.ProbabilityCooperator import ProbabilityCooperator
from strategies.TFTT import TFTTStrategy
from strategies.TitForTatStrategy import TitForTatStrategy
from strategies.AlwaysDefectStrategy import AlwaysDefectStrategy
from strategies.nPavlov import nPavlov


def main():
    # Initialize players/strategies
    player1 = nPavlov(1)
    player2 = ProbabilityCooperator(2)

    # Initialize game
    game = Game(player1, player2, "C", "C")

    # Play game
    rounds = 10000
    for i in range(rounds):
        move1 = player1.play(game)
        move2 = player2.play(game)
        game.play(move1, move2)

    # End game and print results
    print(game.end_game(plot_results=True))


if __name__ == "__main__":
    main()
