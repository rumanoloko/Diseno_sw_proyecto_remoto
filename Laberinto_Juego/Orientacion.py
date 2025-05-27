from typing import override
from abc import abstractmethod

from Laberinto_Juego.Forma import Coordenada2D


class Orientacion:
    def __init__(self):
        pass

    def poner(self, elemento, contenedor):
        raise NotImplementedError

    def recorrer(self, func, forma):
        raise NotImplementedError

    def obtenerElemento(self, forma):
        raise NotImplementedError

    def caminarAleatorio(self, bicho, forma):
        raise NotImplementedError

    def aceptar(self, unVisitor, forma):
        raise NotImplementedError

    def calcularPosicionDesde(self, forma):
        raise NotImplementedError

    def __str__(self):
        return "Soy una orientacion"

class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.norte = elemento

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def __str__(self):
        return "Soy la orientacion norte"

    def obtenerElemento(self, forma):
        return forma.norte

    def caminarAleatorio(self, bicho, forma):
        forma.norte.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.norte.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Coordenada2D(forma.punto.x,forma.punto.y-1)
        forma.norte.calcularPosicionDesdeEn(forma,unPunto)

class Sur(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.sur = elemento

    def recorrer(self, func, contenedor):
        if contenedor.sur is not None:
            func(contenedor.sur)

    def __str__(self):
        return "Soy la orientacion sur"

    def obtenerElemento(self, forma):
        return forma.sur

    def caminarAleatorio(self, bicho, forma):
        forma.sur.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.sur.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Coordenada2D(forma.punto.x,forma.punto.y+1)
        forma.sur.calcularPosicionDesdeEn(forma,unPunto)

class Este(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.este = elemento

    def recorrer(self, func, contenedor):
        if contenedor.este is not None:
            func(contenedor.este)

    def __str__(self):
        return "Soy la orientacion este"

    def obtenerElemento(self, forma):
        return forma.este

    def caminarAleatorio(self, bicho, forma):
        forma.este.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.este.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Coordenada2D(forma.punto.x+1,forma.punto.y)
        forma.este.calcularPosicionDesdeEn(forma,unPunto)

class Oeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.oeste = elemento

    def recorrer(self, func, contenedor):
        if contenedor.oeste is not None:
            func(contenedor.oeste)

    def __str__(self):
        return "Soy la orientacion oeste"

    def obtenerElemento(self, forma):
        return forma.oeste

    def caminarAleatorio(self, bicho, forma):
        forma.oeste.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.oeste.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Coordenada2D(forma.punto.x-1,forma.punto.y)
        forma.oeste.calcularPosicionDesdeEn(forma,unPunto)
