import random
from Laberinto_Juego.Contenedor import Contenedor
from Laberinto_Juego.Herramienta import Herramienta
from Laberinto_Juego.ConcreteComponents import Casco
from Laberinto_Juego.ConcreteComponents import Biblia
from Laberinto_Juego.ConcreteComponents import HuesoBicho
from Laberinto_Juego.ConcreteComponents import Maldicion
from Laberinto_Juego.ConcreteComponents import Brujula
from Laberinto_Juego.Forma import Coordenada2D

class Ataud(Contenedor):
    def __init__(self):
        self._abierto = False
        super().__init__()
        opcion = random.randint(0, 4)
        if opcion == 1:
            herramienta = Maldicion()
            self.añadirHijo(herramienta)
        elif opcion == 2:
            herramienta = Brujula(Coordenada2D(3, 3))
            self.añadirHijo(herramienta)
        elif opcion == 3:
            herramienta = Casco()
            self.añadirHijo(herramienta)
        elif opcion == 4:
            herramienta = Biblia()
            self.añadirHijo(herramienta)

    def abrirCofre(self):
        if not self._abierto:
            herramienta = self.hijos[0]
            self.elminarHijo(self.hijos[0])
            self._abierto = True
            return herramienta
        else:
            print("No se pudeoteer nadad un cofre abierto")
            return

    def __str__(self):
        if self.hijos:
            return "El cofre está abierto y contiene un objeto"
        else:
            return "El cofre está cerrado"
