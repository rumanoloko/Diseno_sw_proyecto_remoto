from abc import ABC, abstractmethod
from Laberinto_Juego.BichoAgresivo import BichoAgresivo
from Laberinto_Juego.Forma import Cuadrado
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta
from Laberinto_Juego import Laberinto
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Ente import Bicho
from Laberinto_Juego.Orientacion import Orientacion, Norte, Sur, Este, Oeste
class Creator:
    def fabricarHabitacion(self, numeroHabitacion: int) -> Habitacion:
        habitacion = Habitacion(numeroHabitacion)
        habitacion.forma = self.fabricarFormaCuadrada()
        paredNorte = self.fabricarPared()
        paredSur = self.fabricarPared()
        paredEste = self.fabricarPared()
        paredOeste = self.fabricarPared()
        habitacion.ponerElementoEnOrientacion(paredNorte, Norte())
        habitacion.ponerElementoEnOrientacion(paredSur, Sur())
        habitacion.ponerElementoEnOrientacion(paredEste, Este())
        habitacion.ponerElementoEnOrientacion(paredOeste, Oeste())

        """
        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        """
        return habitacion

    def fabricarFormaCuadrada(self):
        forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma
    def fabricarLaberinto2FM(self):
        pass

    def fabricarLaberinto2FMD(self):
        pass

    def fabricarPuerta(self) -> Puerta:
        return Puerta()

    def fabricarPared(self) -> Pared:
        return Pared()

    def fabricarAgresivo(self, habitacion: Habitacion)-> Bicho:
        bicho = Bicho()
        bicho.iniAgresivo()
        bicho.posicion = habitacion
        return bicho

    def fabricarPerezoso(self, habitacion: Habitacion)-> Bicho:
        bicho = Bicho()
        bicho.iniPerezoso()
        bicho.posicion = habitacion
        return bicho

    def fabricarNorte(self) -> Orientacion:
        return Norte()

    def fabricarSur(self) -> Orientacion:
        return Sur()

    def fabricarEste(self) -> Orientacion:
        return Este()

    def fabricarOeste(self) -> Orientacion:
        return Oeste()




