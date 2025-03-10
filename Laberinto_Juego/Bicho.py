from abc import ABC, abstractmethod
from typing import override

from Laberinto_Juego.ElementoMapa import ElementoMapa
from Laberinto_Juego.Modo import Modo
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.BichoAgresivo import BichoAgresivo
from Laberinto_Juego.BichoPerezoso import BichoPerezoso

class Bicho(ElementoMapa):
    def __init__(self, vidas: int = 5, modo: Modo = None, poder: int = 1, posicion: Habitacion = None) -> None:
        self._vidas = vidas
        self._modo = modo
        self._poder = poder
        self._posicion = posicion

    @override
    def __str__(self):
        return self.modo
        return "Este es un bicho"

    @property
    def vidas(self):
        return self._vidas

    @property
    def modo(self):
        return self._modo.__str__()

    @property
    def poder(self):
        return self._poder

    @property
    def posicion(self):
        return self._posicion

    @vidas.setter
    def vidas(self, vidas):
        self._vidas = vidas

    @modo.setter
    def modo(self, modo):
        self._modo = modo

    @poder.setter
    def poder(self, poder):
        self._poder = poder

    @posicion.setter
    def posicion(self, posicion):
        self._posicion = posicion

    def esAgresivo(self) -> bool:
        return self._modo.esAgresivo()

    def esPerezoso(self) -> bool:
        return self._modo.esPerezoso()

    def iniAgresivo(self) -> bool:
        self._modo = BichoAgresivo()
        self._poder = 10

    def iniPerezoso(self) -> bool:
        self._modo = BichoPerezoso()
        self._poder = 1

    @override
    def camina(self):
        return "El bicho agresivo camina"

    @override
    def duerme(self):
        return "El bicho agresivo duerme"

    def entrar(self) -> None:
        pass

    def recorrer(self):
        print(self.__str__())