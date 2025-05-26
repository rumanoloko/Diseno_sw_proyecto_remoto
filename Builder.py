from abc import ABC, abstractmethod
from Laberinto_Juego import Tunel
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

    def fabricarTunelEn(self, unContenedor):
        tunel = None
        tunel = Tunel
        unContenedor.agregarHijo(tunel)
