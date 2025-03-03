from typing import override, List
from Laberinto_Juego.Orientacion import Orientacion
from Laberinto_Juego.Contenedor import Contenedor
class Habitacion(Contenedor):
    def __init__(self, numero) -> None:
        super().__init__()
        self._numero = numero
        self._sur = None
        self._norte = None
        self._este = None
        self._oeste = None
        self._orientaciones = {}

    @override
    def añadir(self, unaHabitacion) -> None:
        self.habitaciones.append(unaHabitacion)
    @override
    def entrar(self) -> None:
        pass
    @property
    def orientaciones(self) -> List[Orientacion] | None:
        return self._orientaciones
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

    @orientaciones.setter
    def orientaciones(self, orientaciones:List[Orientacion]) -> None:
        self.orientaciones = orientaciones

    def añadirOrientacion(self, orientacion, elementoOrientacion) -> bool:
        #unaOr ponerElemento:unEM en:self.
        self.orientaciones[orientacion] = elementoOrientacion

    def __str__(self):
        return f"Habitacion {self.numero}"

        #aStream newxtPull:'Hab'; nextPutAll:self

    def entrar(self):
        print('Estas en ', self.__str__())


