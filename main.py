from Game import Game
from strategies.TitForTatStrategy import TitForTatStrategy
from strategies.AlwaysDefectStrategy import AlwaysDefectStrategy


def main():
    # Initialize game
    game = Game()
    # print(game.history[-1].payoffs)

    # Initialize players/strategies
    player1 = TitForTatStrategy(1)
    player2 = AlwaysDefectStrategy(2)

    # Play game
    rounds = 15
    for i in range(rounds):
        move1 = player1.play(game)
        move2 = player2.play(game)
        game.play(move1, move2)
        # print(game.history[-1].payoffs)

    # End game and print results
    print(game.end_game())


if __name__ == "__main__":
    main()
