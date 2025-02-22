#from Laberinto_Juego.Bicho import Bicho
from abc import ABC, abstractmethod
from typing import override


class Modo:

    @override
    def __str__(self):
        pass

    def esAgresivo(self):
        return False

    def esPerezoso(self):
        return False

    def actua(self, unBicho):
        pass

    @abstractmethod
    def caminar(self, unBicho):
        pass

    @abstractmethod
    def dormir(self, unBicho):
        pass

    @abstractmethod
    def atacar(self, unBicho):
        pass