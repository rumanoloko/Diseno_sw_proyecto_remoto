from Laberinto_Juego import Habitacion, Pared, Puerta, Bomba, Tunel
class Visitor:
    def visitarHabitacion(self, habitacion: Habitacion) -> None:
        pass

    def visitarPared(self, pared: Pared) -> None:
        pass

    def visitarPuerta(self, puerta: Puerta) -> None:
        pass

    def visitarBomba(self, bomba: Bomba) -> None:
        pass

    def visitarTunel(self, tunel: Tunel) -> None:
        pass