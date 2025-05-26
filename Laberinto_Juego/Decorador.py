from Laberinto_Juego.Hoja import Hoja
class Decorador(Hoja):
    def __init__(self, component):
        super().__init__()
        self.component = component

    def __str__(self):
        return "Esto es un decorador"
