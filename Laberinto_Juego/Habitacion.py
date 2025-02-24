from typing import override

from Laberinto_Juego.Contenedor import Contenedor
class Habitacion(Contenedor):
    def __init__(self, numero) -> None:
        super().__init__()
        self._numero = numero
        self._sur = None
        self._norte = None
        self._este = None
        self._oeste = None

    @override
    def añadir(self, unaHabitacion) -> None:
        self.habitaciones.append(unaHabitacion)
    @override
    def entrar(self) -> None:
        pass

    @property
    def numero(self):
        return self._numero
    @property
    def sur(self):
        return self._sur
    @property
    def norte(self):
        return self._norte
    @property
    def este(self):
        return self._este
    @property
    def oeste(self):
        return self._oeste

    @numero.setter
    def numero(self, numero) -> None:
        self._numero = numero
    @sur.setter
    def sur(self, sur) -> None:
        self._sur = sur
    @norte.setter
    def norte(self, norte) -> None:
        self._norte = norte
    @este.setter
    def este(self, este) -> None:
        self._este = este
    @oeste.setter
    def oeste(self, oeste) -> None:
        self._oeste = oeste

    def __str__(self):
        return f"Habitacion {self.numero}"


