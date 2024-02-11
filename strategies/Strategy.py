from abc import ABC, abstractmethod
from Game import Game


class Strategy(ABC):
    @abstractmethod
    def __init__(self, player_number: int) -> None:
        self.player_number = player_number

    @abstractmethod
    def play(self, game: Game):
        raise NotImplementedError
