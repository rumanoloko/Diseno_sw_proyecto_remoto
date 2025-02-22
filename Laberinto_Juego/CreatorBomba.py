from Laberinto_Juego import Creator, ParedBomba, Puerta
from Laberinto_Juego.Habitacion import Habitacion


class CreatorBomba(Creator):

    def fabricarPared(self) -> ParedBomba:
        return ParedBomba

    def fabricaHabitacion(self, numeroHabitacion: int):
        habitacion = Habitacion(numeroHabitacion)
        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        return habitacion

    def fabricarLaberinto(self):
        pass