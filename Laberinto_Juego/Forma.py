import random

class Coordenada2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Forma:
    def __init__(self, coordenadaX:int = 0, coordenadaY:int = 0):
        self.orientaciones = []
        self.numero = None
        self.punto = None
        self.coordenada2D = Coordenada2D(coordenadaX, coordenadaY)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def obtenerElementoEnOrientacion(self, orientacion):
        return orientacion.obtenerElemento(self)

    def recorrer(self, func):
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)

    def calcularPosicion(self):
        for orientacion in self.orientaciones:
            orientacion.calcularPosicionDesde(self)
    def caminarAleatorio(self, bicho):
        orientacion=self.obtenerOrientacionAleatoria()
        print(f"Orientacion aleatoria: {orientacion}")
        orientacion.caminarAleatorio(bicho, self)

    def obtenerOrientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def aceptar(self, unVisitor):
        for orientacion in self.orientaciones:
            orientacion.aceptar(unVisitor, self)

class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.orientaciones = []