#from Laberinto_Juego.Juego import Juego
from Laberinto_Juego.Juego import Juego
from Laberinto_Juego.Laberinto import Laberinto
class LaberintoBuilder:
    def __init__(self):
        self._laberinto = None
        self._juego = None
    @property
    def laberinto(self):
        return self.laberinto

    @property
    def juego(self):
        return self.juego

    @laberinto.setter
    def laberinto(self, laberinto):
        self._laberinto = laberinto

    @juego.setter
    def juego(self, juego):
        self._juego = juego

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def __str__(self):
        return "Esto es un Builder de laberinto"

    def metodoFabricacion(self):
        pass

    def fabricarHabitacion(self):
        pass

    def fabricarPuerta(self):
        #fabricarPuertaL1: num1 or1:stOr1 L2:num2 oe2:stOr2
        #|hab1 hab2 obO1 obO2|
        #hab1:= self laberinto ontenerHabitacion num1.
        #hab2:= self laberinto obtenerHabitacion num2.

        #ob0J1:= self perform:('fabricar',stOr1) asSymbol. FABRICAR+nORTE 0> FABRICARnORTE
        #ob0J2:= self perform:('fabricar',stOr2) asSymbol.


        #pt:=Puerta new
        #pt lado1:hab1.
        #pt lado2:hab2.


        #hab1 ponerEnOr1:obOr1
        pass


    #def feabricarJuego(self):
        #self.juego = Juego()

    def fabricarBichoModo(self, unModo, unNum):
        hab1 = None
        bicho = None
        hab = self.laberinto.obtenerHabitacion(unNum)
        #crear el bicho, lo voy a copiar del creator
        #agregar el bicho al juego

    def fabricarJuego(self):
        self.juego = Juego()
        self.juego.prototipe(self, self.laberinto)
        self.juego.laberinto(self, self.laberinto.deepCopy) #self.juego clonaLaberinto




