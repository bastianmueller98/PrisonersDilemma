from src.Game import Game
from src.strategies.ProbabilityCooperator import ProbabilityCooperator
from src.strategies.TFTT import TFTTStrategy
from src.strategies.TitForTatStrategy import TitForTatStrategy
from src.strategies.AlwaysDefectStrategy import AlwaysDefectStrategy
from src.strategies.nPavlov import nPavlov


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
    print(game.end_game(plot_results=True, save_fig=True))


if __name__ == "__main__":
    main()
