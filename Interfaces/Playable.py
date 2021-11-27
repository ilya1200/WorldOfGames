from abc import ABC, abstractmethod
from typing import Any


class Playable(ABC):

    @abstractmethod
    def play(self, *args, **kwargs) -> Any:
        pass
