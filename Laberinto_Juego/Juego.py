import sys
import time
from operator import truediv
from typing import TYPE_CHECKING

from Laberinto_Juego.Forma import Coordenada2D
from Laberinto_Juego.HahitacionGUI import HabitacionGUI
from Laberinto_Juego.Gui import Gui
#from Laberinto_Juego.Creator import Creator
#from Laberinto_Juego.Ente import Bicho
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Contenedor import Contenedor
from Laberinto_Juego import Laberinto
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta
from Laberinto_Juego.Orientacion import Orientacion, Norte, Sur, Este, Oeste
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

if TYPE_CHECKING:
    from Laberinto_Juego.Ente import Bicho

#from Laberinto_Juego.Laberinto import Laberinto

#from Laberinto_Juego.Director import Director
#from Laberinto_Juego.Creator import Creator


class Juego:
    #from Laberinto_Juego.Ente import Bicho
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []
        self.personaje = None
        self.gui = Gui()
        self.ventana = None


    def iniciarJuego(self, dict):
        #self.bichos[0].start()
        #self.gui.mostrar_laberinto(dict, self.personaje.posicion.numero)
        for bicho in self.bichos:
            #pass
            bicho.start()
        #self.personaje.start()
        self.iniciarInterfaz()
        #print(self.personaje.posicion)
        #print(self.personaje.vidas)
        #print(self.personaje.poder)
        #print(self.personaje.estadoEnte.vivir(self.personaje))

    def iniciarInterfaz(self):
        app = QApplication(sys.argv)
        self.ventana = HabitacionGUI(self)
        self.ventana.show()
        sys.exit(app.exec())

    def refrestarInterfaz(self):
        if self.ventana is not None:
            self.ventana.dibujar_habitacion()

    def agregarPersonaje(self, nombre, vidas, poder, posicion, juego, estadoEnte):
        from Laberinto_Juego.Ente import Personaje
        #"Petru-Vlad Pasat", 10, 4, juego.laberinto.hijos[0], juego, Vivo()
        self.personaje = Personaje(nombre, vidas, poder, posicion, juego, estadoEnte)
        posicion.añadirHijo(self.personaje)

    def actualizarPosicionJugador(self, tecla):
        resultado = self.personaje.actualizarPosicion(tecla)
        return resultado

    def buscarEnemigo(self, ente):
        if ente.posicion.numero == self.personaje.posicion.numero and self.personaje.estadoEnte.__class__.__name__ == "Vivo":
            self.personaje.esAtacadoPor(ente)
            ente.esAtacadoPor(self.personaje)
            return True
        return False
        self.ventana.dibujar_habitacion()
        self.ventana.mostrar_laber()

    def crearLaberinto4Hab4BichosFM(self, unFM = None) -> tuple():
        hab1 = unFM.fabricarHabitacion([0,0])
        hab2 = unFM.fabricarHabitacion([0,1])
        hab3 = unFM.fabricarHabitacion([1,0])
        hab4 = unFM.fabricarHabitacion([1,1])
        puerta1 = unFM.fabricarPuerta()
        puerta2 = unFM.fabricarPuerta()
        puerta3 = unFM.fabricarPuerta()
        puerta4 = unFM.fabricarPuerta()
        bichoA1 = unFM.fabricarAgresivo(hab1)
        bichoA2 = unFM.fabricarAgresivo(hab2)
        bichoP1 = unFM.fabricarPerezoso(hab3)
        bichoP2 = unFM.fabricarPerezoso(hab3)

        bichoA1.posicion = hab1
        bichoA2.posicion = hab2
        bichoP1.posicion = hab3
        bichoP2.posicion = hab4

        puerta1.lado1 = hab1
        puerta1.lado2 = hab2
        hab1.este = puerta1
        hab2.oeste = puerta1

        puerta2.lado1 = hab2
        puerta2.lado2 = hab4
        hab2.sur = puerta2
        hab4.norte = puerta2

        puerta3.lado1 = hab4
        puerta3.lado2 = hab3
        hab4.oeste = puerta3
        hab3.este = puerta3

        puerta4.lado1 = hab3
        puerta4.lado2 = hab1
        hab3.norte= puerta4
        hab1.sur = puerta4

        hab1.ponerElementoEnOrientacion(puerta1, Este())
        hab1.ponerElementoEnOrientacion(puerta4, Sur())
        hab3.ponerElementoEnOrientacion(puerta3, Este())
        hab3.ponerElementoEnOrientacion(puerta4, Norte())
        hab2.ponerElementoEnOrientacion(puerta1, Oeste())
        hab2.ponerElementoEnOrientacion(puerta2, Sur())
        hab4.ponerElementoEnOrientacion(puerta2, Norte())
        hab4.ponerElementoEnOrientacion(puerta3, Oeste())

        laberinto = Laberinto()
        laberinto.añadirHijo(hab1)
        laberinto.añadirHijo(hab2)
        laberinto.añadirHijo(hab3)
        laberinto.añadirHijo(hab4)
        hab1.añadirHijo(bichoA1)
        hab2.añadirHijo(bichoA2)
        hab3.añadirHijo(bichoP1)
        hab4.añadirHijo(bichoP2)


        puerta1.abierta = True
        puerta2.abierta = True
        puerta3.abierta = True
        puerta4.abierta = True
        return laberinto, [bichoA1, bichoA2, bichoP1, bichoP2]


    def fabricarLaberinto(self):
        laberinto = Laberinto()
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        laberinto.hijos.append(hab1)
        laberinto.hijos.append(hab2)
        puerta = Puerta(True)
        hab1.sur = puerta
        hab2.norte = puerta
        return laberinto

    def obtenerHabitacionPorNumero(self, numero):
        for habitacion in self.labetinro.hijos:
            if habitacion.numero == numero:
                return habitacion
        return False
    def buscarPersonaje(self, unBicho):
        for contenido in self.bicho.posicion.hijos:
            if contenido.__class__.__name__() == 'Personaje':
                contenido
        return False

    def gestionBichos(self):
        for bicho in self.bichos:
            bicho.start()

    def agregarBicho(self, bicho) -> None:
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho) -> None:
        if bicho in self.bichos:
            self.bichos.remove(bicho)
            return True
        else:
            return False
