from Habitacion import Habitacion

class Laberinto:
    def __init__(self):
        self.habitaciones = []

    def __str__(self):
        return "Este es un laberinto"

    def entrar(self) -> None:
        print("Entrar en la habitacion 1")

    def eliminarHabitacion(self, unaHabitacion:Habitacion) -> None:
        absent = True
        if (unaHabitacion in self.habitaciones):
            self.habitaciones.remove(unaHabitacion)
            absent = False

        if absent:
            pass

    def agregarHabitacion(self, unaHabitacion: Habitacion) -> None:
        if(unaHabitacion not in self.habitaciones):
            self.habitaciones.append(unaHabitacion)
