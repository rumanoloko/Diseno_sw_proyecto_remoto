from Laberinto_Juego.Pared import Pared
class ParedBomba(Pared):
    def __init__(self, estado: bool = False) -> None:
        self.activa = estado

    def __str__(self) -> None:
        return "Esta es una pared bomba"
