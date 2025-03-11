from typing import override
from Laberinto_Juego.Habitacion import Habitacion

class Ente:
    def __init__(self, vidas, poder, posicion:Habitacion = None) -> None:
        self._vidas = vidas
        self.poder = poder
        self._posicion = posicion

    @property
    def vidas(self):
        return self._vidas
    @vidas.setter
    def vidas(self, vidas):
        self._vidas = vidas

    @property
    def poder(self):
        return self._posicion
    @poder.setter
    def poder(self, poder):
        self._posicion = poder

    @property
    def posicion(self):
        return self._posicion
    @posicion.setter
    def posicion(self, posicion):
        self._posicion = posicion


