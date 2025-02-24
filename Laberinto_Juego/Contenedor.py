from typing import Any

from Laberinto_Juego.ElementoMapa import ElementoMapa
class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self._hijos: list() = []
        self._padre:Any = None

    def añadirHijo(self, hijo) -> bool:
        if hijo in self.hijos:
            return False
        hijo.padre = self
        self.hijos.append(hijo)
        return True

    def eliminarHijo(self, hijo) -> bool:
        if hijo in self.hijos:
            return True
        self.hijos.remove(hijo)
        return False

    def __str__(self):
        return "Es un elemento mapa que tiene hijos"
    @property
    def hijos(self):
        return self._hijos

    @hijos.setter
    def hijos(self, hijos):
        self._hijos = hijos

    @property
    def padre(self):
        return self._padre

    @padre.setter
    def padre(self, padre):
        self._padre = padre

