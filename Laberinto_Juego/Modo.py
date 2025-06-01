#from Laberinto_Juego.Bicho import Bicho
from abc import ABC, abstractmethod
from typing import override


class Modo:
    @abstractmethod
    def __str__(self):
        pass

    def esAgresivo(self):
        return False

    def esPerezoso(self):
        return False

    def esInformatico(self):
        return False

    def actua(self, unBicho):
        pass

    def caminar(self, unBicho):
        unBicho.obtenerOrientacion()

    @abstractmethod
    def dormir(self, unBicho):
        pass

    @abstractmethod
    def atacar(self, unBicho):
        pass