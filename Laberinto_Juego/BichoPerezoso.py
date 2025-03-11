from typing import override

from Laberinto_Juego.Modo import Modo

class BichoPerezoso(Modo):
    _numero = 0

    def __init__(self):
        self._numero = BichoPerezoso._numero
        BichoPerezoso._numero +=1
    @override
    def __str__(self):
        return f"Bicho perezoso {self._numero}"

    def esPerezoso(self):
        return True


    def duerme(self):
        return "Bicho agresivo duerme"