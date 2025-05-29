from __future__ import annotations

from abc import abstractmethod
from typing import List, Any
from Laberinto_Juego.ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self._hijos: List[Any] = []
        self._padre: Contenedor | None = None  # Puede ser Contenedor o None
        self.forma = None

    def añadirHijo(self, hijo) -> bool:
        if hijo in self.hijos:
            return False
        hijo.padre = self
        self.hijos.append(hijo)
        return True

    def eliminarHijo(self, hijo: ElementoMapa) -> bool:
        if hijo in self.hijos:
            self.hijos.remove(hijo)
            return True
        return False

    @abstractmethod
    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)

        self.forma.recorer(func)

    def aceptar(self, visitante):
        self.aceptarVisitante(visitante)
        for hijo in self.hijos:
            hijo.aceptar(visitante)
        self.forma.aceptar(visitante)

    def caminarRandom(self, bicho):
        self.forma.caminarAleatorio(bicho)

    def agregarOrientacion(self, orientacion):
        self.forma.agregarOrientacion(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.forma.eliminarOrientacion(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        self.forma.ponerElementoEnOrientacion(elemento, orientacion)

    def __str__(self) -> str:
        return "Es un elemento mapa que tiene hijos"





    @property
    def hijos(self) -> List[ElementoMapa]:
        return self._hijos

    @hijos.setter
    def hijos(self, hijos: List[ElementoMapa]) -> None:
        self._hijos = hijos

    @property
    def padre(self) -> Contenedor | None:
        return self._padre

    @padre.setter
    def padre(self, padre: Contenedor | None) -> None:
        if padre is not None and not isinstance(padre, Contenedor):
            raise TypeError("padre debe ser un objeto Contenedor o None")
        self._padre = padre
