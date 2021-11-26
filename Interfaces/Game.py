from abc import ABCMeta

from Interfaces.Playable import Playable


class Game(Playable, metaclass=ABCMeta):
    pass


