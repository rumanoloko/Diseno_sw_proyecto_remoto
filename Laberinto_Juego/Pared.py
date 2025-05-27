from abc import ABC, abstractmethod
from Laberinto_Juego.ElementoMapa import ElementoMapa


class Pared(ElementoMapa):
    def __init__(self):
        pass

    def __str__(self):
        return "Esta es una pared normal"

    def entrar(self):
        print("Orco, chocaste con una pared")

    def recorrer(self, func):
        func(self.__str__())
