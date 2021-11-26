from abc import ABCMeta, abstractmethod
from Interfaces.Playable import Playable


class Game(Playable, metaclass=ABCMeta):

    @abstractmethod
    def play(self, *args, **kwargs) -> bool:
        """
        :return: Represents a game result Win or Lose
        """
        pass


