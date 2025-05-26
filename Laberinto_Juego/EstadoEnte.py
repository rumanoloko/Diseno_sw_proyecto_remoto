"""
from typing import override
from Laberinto_Juego.Ente import Ente

class EstadoEnte:
    def __init__(self)  -> None:
        pass
    def vivir(self, ente: Ente) -> None:
        pass

    def morir(self, ente: Ente) -> None:
        pass


class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()

    @override(EstadoEnte)
    def vivir(self,ente: Ente) -> None:
        print("El ente ya está vivo")

    @override(EstadoEnte)
    def morir(self, ente: Ente):
        print("El ente muere")
        ente.estadoEnte = Muerto()

class Muerto(EstadoEnte):

    def __init__(self):
        super().__init__()

    @override(EstadoEnte)
    def vivir(self, ente: Ente) -> None:
        print("El ente revive")
        ente.estadoEnte = Vivo()

    @override(EstadoEnte)
    def morir(self, ente: Ente) -> None:
        print("No se puede morir algo ya muerto")
"""


