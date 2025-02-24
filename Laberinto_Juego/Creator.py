from abc import ABC, abstractmethod
from Laberinto_Juego.BichoAgresivo import BichoAgresivo
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta
from Laberinto_Juego import Laberinto
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Bicho import Bicho

class Creator(ABC):
    def fabricarHabitacion(self, numeroHabitacion: int) -> Habitacion:
        habitacion = Habitacion(numeroHabitacion)
        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        return habitacion

    def fabricarPuerta(self) -> Puerta:
        return Puerta()

    def fabricarPared(self) -> Pared:
        return Pared()

    def fabricarAgresivo(self)-> Bicho:
        bicho = Bicho()
        bicho.iniAgresivo()
        return bicho

    def fabricarPerezoso(self)-> Bicho:
        bicho = Bicho()
        bicho.iniPerezoso()
        return bicho



