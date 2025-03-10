from typing import override

from Laberinto_Juego.Modo import Modo


class BichoAgresivo(Modo):

    @override
    def __str__(self):
        return "Bicho agresivo"

    def esAgresivo(self) -> bool:
        return True

    def camina(self):
        return "Bicho agresivo camina"

    def duerme(self):
        return "Bicho agresivo duerme"
