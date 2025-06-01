import random
from typing import override

from Laberinto_Juego import Personaje
from Laberinto_Juego.Forma import Coordenada2D
from Laberinto_Juego.Hoja import Hoja
from Laberinto_Juego.Herramienta import Herramienta

class Casco(Herramienta):
    _reductorDaño = 1
    def __init__(self):
        super().__init__()

    @override
    def asignarPortador(self, personaje: Personaje):
        self.portador = personaje
        self.portador.reductorDaño += Casco._reductorDaño
    @override
    def desasignarPortador(self):
        self.portador = None
        self.portador.reductorDaño -= Casco._reductorDaño

class Biblia(Herramienta):
    _aura = 2
    def __init__(self):
        super().__init__()

    @override
    def asignarPortador(self, personaje: Personaje):
        self.portador = personaje
        self.portador.aura += Biblia._aura
    @override
    def desasignarPortador(self):
        self.portador = None
        self.portador.aura -= Biblia._reductorDaño

class HuesoBicho(Herramienta):
    _daño = 1
    def __init__(self):
        super().__init__()
        self.numeroUsos = 3

    @override
    def asignarPortador(self, personaje: Personaje):
        self.portador = personaje
        self.portador.daño += HuesoBicho._daño

    @override
    def desasignarPortador(self):
        self.portador = None
        self.portador.daño -= HuesoBicho._daño

    def desgastarHueso(self):
        self.numeroUsos -= 1
        if self.numeroUsos == 0:
            self.desasignarPortador()

class Maldicion(Herramienta):

    _penalizacionDaño = 0
    _penalizacionVidas = 0
    def __init__(self):
        super().__init__()
        penalizacion = random.randint(1, 2)
        if penalizacion == 1:
            Maldicion._penalizacionVidas = 2
            Maldicion._penalizacionDaño = 0
        else:
            Maldicion._penalizacionVidas = 0
            Maldicion._penalizacionDaño = 2


    @override
    def asignarPortador(self, personaje: Personaje):
        self.portador = personaje
        self.portador.vidas -= Maldicion._penalizacionVidas
        self.portador.poder -= Maldicion._penalizacionPoder

    @override
    def desasignarPortador(self):
        self.portador = None
        self.portador.vidas += Maldicion._penalizacionVidas
        self.portador.poder += Maldicion._penalizacionPoder





class Brujula(Herramienta):
    _destino = [3, 3]
    def __init__(self, posicionDestino: Coordenada2D):
        _destino = posicionDestino

    @override
    def asignarPortador(self, personaje: Personaje):
        self.portador = personaje

    @override
    def desasignarPortador(self):
        self.portador = None

    @staticmethod
    def verBrujula(posicion_actual):
        actual_x, actual_y = posicion_actual
        destino_x, destino_y = Brujula._destino

        if (actual_x, actual_y) == Brujula._destino:
            print("Ya estas en el destino")
            return

        sentido = None

        if actual_y < destino_y and actual_x == destino_x:
            sentido = "norte"
        elif actual_y < destino_y and actual_x < destino_x:
            sentido = "noroeste"
        elif actual_y < destino_y and actual_x > destino_x:
            sentido = "noreste"

        if actual_y > destino_y and actual_x == destino_x:
            sentido = "sur"
        elif actual_y < destino_y and actual_x < destino_x:
            sentido = "suroeste"
        elif actual_y < destino_y and actual_x > destino_x:
            sentido = "sureste"

        if actual_y == destino_y and actual_x > destino_x:
            sentido = "oeste"
        elif actual_y == destino_y and actual_x < destino_x:
            sentido = "este"

        print(f"Desde {posicion_actual}, debes moverte en sentido {sentido}")
