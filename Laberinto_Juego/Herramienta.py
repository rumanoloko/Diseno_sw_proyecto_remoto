from Laberinto_Juego.Hoja import Hoja
from Laberinto_Juego.Ente import Personaje

class Herramienta(Hoja):
    def __init__(self):
        self.portador = None

    def asignarPortador(self, portador: Personaje):
        pass
    def desasignarPortador(self):
        pass