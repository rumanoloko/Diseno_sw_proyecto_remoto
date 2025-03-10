from typing import override

from Laberinto_Juego.Modo import Modo

class BichoPerezoso(Modo):

    @override
    def __str__(self):
        return "Bicho perezoso"

    def esPerezoso(self):
        return True

    def camina(self):
        pass

    def camina(self):
        return "Bicho agresivo camina"

    def duerme(self):
        return "Bicho agresivo duerme"