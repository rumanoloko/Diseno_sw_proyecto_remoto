from Laberinto_Juego.Ente import Ente
from Laberinto_Juego.Habitacion import Habitacion
class Personaje(Ente):
    def __init__(self, nombre, vidas=20, poder=10, posicion: Habitacion = None) -> None:
        super().__init__(vidas, poder, posicion)
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def esAtacadoUnBicho(self, unBicho):
        print("Alguien es atacado por ", unBicho)
        self.vidas -= unBicho.poder
        print("Vidas: ", self.vidas)
        if self.vidas <= 0:
            self.finJuego()

    def finJuego(self):
        pass

    #personaje debega en contenedor, contenedor delega en orientacion
    #no hace falta delegar en orietaciones, contenedor ya conoce las orientaciones
    def __str__(self):
        return "Soy el personaje ",self._nombre, " y estoy en ", self.orientacion


    def irNorte(self):
        puerta = self.orientacion
        #self posicion irAlNorte self.
        self.posicion.irAlNorte(self)

    def irSur(self):
        self.posicion.irAlSur(self)

    def irEste(self):
        self.posicion.irAlEste(self)

    def irOeste(self):
        self.posicion.irAlOeste(self)