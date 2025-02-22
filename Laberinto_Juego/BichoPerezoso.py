from typing import override

from Laberinto_Juego.Modo import Modo

class BichoPerezoso(Modo):

    @override
    def __str__(self):
        return "Este es un bicho perezoso"

    def esPerezoso(self):
        return True