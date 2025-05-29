from typing import TYPE_CHECKING

from Laberinto_Juego.Gui import Gui
#from Laberinto_Juego.Creator import Creator
#from Laberinto_Juego.Ente import Bicho
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Contenedor import Contenedor
from Laberinto_Juego import Laberinto
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta
from Laberinto_Juego.Orientacion import Orientacion, Norte, Sur, Este, Oeste

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

    def iniciarJuego(self, dict):
        #self.bichos[0].start()
        self.gui.mostrar_laberinto(dict, self.personaje.posicion.numero)
        for bicho in self.bichos:
            pass
            #bicho.start()
        self.personaje.start()
        #print(self.personaje.posicion)
        #print(self.personaje.vidas)
        #print(self.personaje.poder)
        #print(self.personaje.estadoEnte.vivir(self.personaje))


    def agregarPersonaje(self, nombre, vidas, poder, posicion, juego, estadoEnte):
        from Laberinto_Juego.Ente import Personaje
        #"Petru-Vlad Pasat", 10, 4, juego.laberinto.hijos[0], juego, Vivo()
        self.personaje = Personaje(nombre, vidas, poder, posicion, juego, estadoEnte)

    def actualizarPosicionJugador(self, tecla):
        resultado = self.personaje.actualizarPosicion(tecla)
        return resultado

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

    def obtenerHabitacionPorNumero(self):
        pass

    def buscarEnemigo(self):
        pass

    def buscarPersonaje(self, unBicho):
        pass

    def gestionBichos(self):
        pass

    def agregarBicho(self, bicho) -> None:
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho) -> None:
        hayBicho = False
        if bicho in self.bichos:
            self.bichos.remove(bicho)
        else:
            pass
            #raise error
