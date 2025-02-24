from typing import Any

from Habitacion import Habitacion
from Laberinto_Juego.ElementoMapa import ElementoMapa
from Laberinto_Juego.Contenedor import Contenedor
class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Esto es un laberinto"

    def entrar(self) -> None:
        print("Entrar en la habitacion 1")

    def eliminarHabitacion(self, unaHabitacion:Habitacion) -> None:
        absent = True
        if (unaHabitacion in self.hijos):
            self.hijos.remove(unaHabitacion)
            absent = False

        if absent:
            pass

    def agregarHabitacion(self, unaHabitacion: Habitacion) -> None:
        if(unaHabitacion not in self.hijos):
            self.hijos.append(unaHabitacion)

    def obtenerHabitacion(self, numHabitacion:int) -> Any:
        return self.hijos[numHabitacion]
