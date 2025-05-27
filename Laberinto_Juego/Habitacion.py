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
    def añadirOrientacion(self, orientacion, elementoOrientacion) -> bool:
        #unaOr ponerElemento:unEM en:self.
        self.orientaciones[orientacion] = elementoOrientacion

    def __str__(self):
        return f"Habitacion {self.numero}"

        #aStream newxtPull:'Hab'; nextPutAll:self

    def entrar(self, alguien):
        print('Estas en ', self.__str__())
        alguien.posicion = self

    @override
    def recorrer(self, func):
        print(self.__str__())
        #print(self.hijos)
        for x in self.hijos:
            x.recorrer(func)

    def irAlSur(self, alguien):
        #self sur entrar:alguien
        self.sur.entrar(alguien)
            #el personaje x esta en habx
            #chocaste con una pared
            #la puerta está cerrada

    def irAlNorte(self, alguien):
        #self sur entrar:alguien
        self.norte.entrar(alguien)

    def irAlEste(self, alguien):
        #self sur entrar:alguien
        self.este.entrar(alguien)

    def irAlOeste(self, alguien):
        #self sur entrar:alguien
        self.oeste.entrar(alguien)

    @override
    def añadir(self, unaHabitacion) -> None:
        self.habitaciones.append(unaHabitacion)
    def añadir(self, orientacion, elemento):
        if orientacion == "Sur":
            self._sur = elemento
        if orientacion == "Norte":
            self._norte = elemento
        if orientacion == "Este":
            self._este = elemento
        if orientacion == "Oeste":
            self._oeste = elemento
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



