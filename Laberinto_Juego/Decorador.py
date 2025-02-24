from Laberinto_Juego.Hoja import Hoja
class Decorador(Hoja):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Esto es un decorador"
