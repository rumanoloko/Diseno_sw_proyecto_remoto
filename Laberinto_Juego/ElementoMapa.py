from abc import ABC, abstractmethod
class ElementoMapa(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def entrar(self) -> None:
        pass

    @abstractmethod
    def recorrer(self, func):
        pass