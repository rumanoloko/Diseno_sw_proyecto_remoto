from abc import ABC

from AbstractFactory import fabricarPared
from Laberinto_Juego import Habitacion, Puerta, Laberinto, Pared, Juego, BichoPerezoso
from Laberinto_Juego.Bicho import Bicho
from Laberinto_Juego.BichoAgresivo import BichoAgresivo


class FactoryMethod(ABC):
    def fabricaHabitacion(self, numeroHabitacion):
        habitacion = Habitacion(numeroHabitacion)
        habitacion.norte = fabricarPared()
        habitacion.este = fabricarPared()
        habitacion.oeste = fabricarPared()
        habitacion.sur = fabricarPared()
        return habitacion

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarPuerta(self):
        return Puerta()

    def fabricarPared(self):
        return Pared()

    def fabricarBichoAgresivo(self) -> Bicho:
        bicho = Bicho()
        bicho.modo = BichoAgresivo
        bicho.poder = 5
        return bicho

    def fabricarBichoPerezoso(self) -> Bicho:
        bicho = Bicho()
        bicho.modo = BichoPerezoso
        return bicho

    def cambiarModoAgresivo(self, unBicho:Bicho) -> Bicho:
        unBicho.modo = BichoAgresivo
        unBicho.poder = 5
        unBicho.vidas = 5
        unBicho.posicion = None
        return unBicho

    def cambiarModoPerezoso(self, unBicho:Bicho) -> Bicho:
        unBicho.modo = BichoPerezoso
        unBicho.poder = 1
        unBicho.vidas = 1
        unBicho.posicion = None
        return unBicho

