from Laberinto_Juego import Habitacion
from typing import Any
class Puerta:

    def __init__(self, estado :bool = False):
        self._abierta = estado
        self._lado1 = None
        self._lado2 = None

    @property
    def abierta(self) -> bool:
        return self._abierta
    @property
    def lado1(self) -> Any:
        return self._lado1
    @property
    def lado2(self) -> Any:
        return self._lado2


    @abierta.setter
    def abierta(self, estado: bool) -> bool:
        self._abierta = estado
    @lado1.setter
    def lado1(self, lado:Habitacion) -> Any:
        self._lado1 = lado
    @lado2.setter
    def lado2(self, lado:Habitacion) -> Any:
        self._lado2 = lado

    def __str__(self):
        return "La puerta está abierta" if self.abierta else "La puerta está cerrada"
