from typing import override

from Laberinto_Juego.Modo import Modo


class BichoAgresivo(Modo):

    @override
    def __str__(self):
        return "Este es un bicho agresivo"

    def esAgresivo(self) -> bool:
        return True