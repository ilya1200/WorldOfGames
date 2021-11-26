from abc import ABC, abstractmethod


class Playable(ABC):

    @abstractmethod
    def play(self) -> bool:
        pass
