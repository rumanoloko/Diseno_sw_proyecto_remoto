from Laberinto_Juego.Hoja import Hoja
from Laberinto_Juego.Visitor import Visitor

class Tunel(Hoja):
    def __init__(self):
        self._laberinto = None

    def aceptar(self, unVisitante: Visitor):
        unVisitante.visitarTunel(self)


    def entrar(self, alguien):
        # self laberinto:alguien juego prototipo deepCopy.
        "el personaje crea un nuevo laberinto y entra en él"
        if self.laberinto is None:
            alguien.clonarLaberinto(self)
        else:
            self.laberinto.entrar(alguien)


    def __str__(self):
        return "Es un proxy virtual. En principio el personaje creará un nuevo laberinto cuando entre en el tunel"

    @property
    def laberinto(self):
        return self._laberinto

    @laberinto.setter
    def laberinto(self, laberinto):
        self._laberinto = laberinto