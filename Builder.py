from abc import ABC, abstractmethod

class Builder(ABC):

    @property
    @abstractmethod
    def producto(self) -> None:
        pass

    def añadirParedes(self) -> None:
        pass

    def añadirPuertas(self) -> None:
        pass

    def añadirCriaturas(self) -> None:
        pass
