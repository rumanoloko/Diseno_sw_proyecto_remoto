from typing import override

from Laberinto_Juego.Modo import Modo


class BichoAgresivo(Modo):
    _numero = 0
    def __init__(self):
        super().__init__()
        self._numero = BichoAgresivo._numero
        BichoAgresivo._numero +=1

    @override
    def __str__(self):
        return f"Bicho agresivo {self._numero}"

    def esAgresivo(self) -> bool:
        return True

    def duerme(self):
        return "Bicho agresivo duerme"
