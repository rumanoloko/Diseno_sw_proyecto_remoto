import string
import threading
import random
import time
from typing import override, TYPE_CHECKING
from Laberinto_Juego import Habitacion, Puerta
#from Laberinto_Juego.EstadoEnte  import EstadoEnte
from Laberinto_Juego.BichoAgresivo import BichoAgresivo
from Laberinto_Juego.BichoInformatico import BichoInformatico
from Laberinto_Juego.BichoPerezoso import BichoPerezoso
from Laberinto_Juego import Tunel
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta
import keyboard
import os, sys
class EstadoEnte:
    def __init__(self)  -> None:
        pass


    def vivir(self, ente):
        pass

    def morir(self, ente) -> None:
        pass


class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()


    def vivir(self,ente):
        print("El ente ya está vivo")


    def morir(self, ente):
        print("El ente muere")
        ente.estadoEnte = Muerto()

class Muerto(EstadoEnte):

    def __init__(self):
        super().__init__()


    def vivir(self, ente) -> None:
        print("El ente revive")
        ente.estadoEnte = Vivo()

    def morir(self, ente) -> None:
        print("No se puede morir algo ya muerto")

class Ente:
    from Laberinto_Juego import Juego
    """
    if TYPE_CHECKING:
        from Laberinto_Juego.Juego import Juego
    """

    def __init__(self, vidas: int, poder: int, posicion:Habitacion=None, juego:Juego = None, estadoEnte: EstadoEnte = Vivo()) -> None:
        self._vidas = vidas
        self._poder = poder
        self._posicion = posicion
        self._juego = juego
        self._estadoEnte = estadoEnte
        self.aura = 0
        self.reductorDaño = 0


    def esAtacadoPor(self, atacante):
        print(f"{self} es atacado por {atacante}")
        self._vidas -= (atacante.poder - self.reductorDaño)
        if self.vidas < 0:
            self.vidas = 0
        print(f"A {self} le quedan {self._vidas}")
        if self._vidas <= 0:
            print(f"{self} a muerto")
            self.estadoEnte.morir(self)
        #print(self.estadoEnte.__class__.__name__)


    @property
    def vidas(self):
        return self._vidas
    @vidas.setter
    def vidas(self, vidas):
        self._vidas = vidas
    @property
    def poder(self):
        return self._poder
    @poder.setter
    def poder(self, poder):
        self._poder = poder

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, posicion):
        self._posicion = posicion

    @property
    def juego(self):
        return self._juego

    @juego.setter
    def juego(self, juego):
        self._juego = juego

    @property
    def estadoEnte(self):
        return self._estadoEnte

    @estadoEnte.setter
    def estadoEnte(self, estadoEnte):
        self._estadoEnte = estadoEnte


import threading
import random

import threading
import random

class Bicho(Ente):
    _numero = 0
    _lock = threading.Lock()

    def __init__(self, modo=None, posicion: Habitacion = None, vidas: int = 5, poder: int = 1) -> None:
        super().__init__(vidas, poder, posicion)
        self._numero = Bicho._numero
        Bicho._numero += 1
        self.modo = modo
        self._running = False
        self._timer = None
        self._enemigo_timer = None

    def start(self):
        if self._posicion is None:
            with Bicho._lock:
                print(f"Error: No se puede iniciar {self} porque no tiene una posición asignada.")
            return

        with Bicho._lock:
            print(f"{self} ha comenzado en {self.posicion}")

        self._running = True
        self.start_camina()
        self.start_buscar_enemigo()

    def stop(self):
        self.stop_camina()
        self.stop_buscar_enemigo()
        self._running = False

    def start_camina(self):
        if self._running:
            self._mover_bicho()

    def stop_camina(self):
        if self._timer:
            self._timer.cancel()

    def _mover_bicho(self):
        if self._running:
            self.camina()
            self._timer = threading.Timer(3, self._mover_bicho)
            self._timer.start()

    def start_buscar_enemigo(self):
        if self._running:
            self._buscar_enemigo_periodico()

    def stop_buscar_enemigo(self):
        if self._enemigo_timer:
            self._enemigo_timer.cancel()

    def _buscar_enemigo_periodico(self):
        if not self._running:
            return

        if self.estadoEnte.__class__.__name__ == "Vivo":
            with Bicho._lock:
                self.atacarPersonaje()

        # Reprograma la siguiente ejecución
        self._enemigo_timer = threading.Timer(3.5, self._buscar_enemigo_periodico)
        self._enemigo_timer.start()

    def camina(self):
        if not self.posicion:
            with Bicho._lock:
                print(f"Error: {self} no tiene una posición inicial válida.")
            return

        opciones = [self.posicion.norte, self.posicion.oeste, self.posicion.este, self.posicion.sur]
        opciones = [o for o in opciones if o]

        if not opciones:
            with Bicho._lock:
                print(f"{self} está atrapado y no puede moverse.")
            return

        neo_posicion = random.choice(opciones)

        with Bicho._lock:
            """
            if isinstance(neo_posicion, Pared):
                #print(f"El subnormal del {self} chocó con una pared en {self._posicion}")
                print(f"{self} está en {self._posicion}")
            elif isinstance(neo_posicion, Puerta):
                if neo_posicion.abierta:
                    self.posicion.eliminarHijo(self)
                    if neo_posicion.lado1.numero == self.posicion.numero:
                        self.posicion = neo_posicion.lado2
                    else:
                        self.posicion = neo_posicion.lado1
                    print(f"{self} está en {self._posicion}")
                else:
                    print(f"{self} no puede avanzar por la puerta cerrada en {self._posicion}.")
            else:
                self.posicion = neo_posicion
                print(f"{self} se ha movido a {self.posicion}")
            """
    def atacarPersonaje(self):
        self.juego.buscarEnemigo(self)


    def iniAgresivo(self):
        self.modo = BichoAgresivo()
        self._poder = 2

    def iniPerezoso(self):
        self.modo = BichoPerezoso()
        self._poder = 1

    def iniInformatico(self):
        self.modo = BichoInformatico()
        self._poder = 4

    def recorrer(self, func):
        with Bicho._lock:
            func(self)

    def __str__(self):
        return self.modo.__str__()


class Personaje(Ente):
    from Laberinto_Juego.Juego import Juego
    def __init__(self, nombre: string, vidas: int = 10, poder: int = 4, posicion:Habitacion = None, juego:Juego = None, estadoEnte: EstadoEnte = Vivo()) -> None:
        super().__init__(vidas, poder, posicion, juego, estadoEnte)
        self.nombre = nombre
        self.inventario = []

    def actualizarPosicionJugador(self, tecla):
        diccionarioOrientaciones = {}
        diccionarioOrientaciones['w'] = self.posicion.norte
        diccionarioOrientaciones['s'] = self.posicion.sur
        diccionarioOrientaciones['d'] = self.posicion.este
        diccionarioOrientaciones['a'] = self.posicion.oeste

        if tecla in diccionarioOrientaciones and isinstance(diccionarioOrientaciones[tecla], Puerta) and diccionarioOrientaciones[tecla].abierta:
            if diccionarioOrientaciones[tecla].lado1.numero == self.posicion.numero:
                self.posicion = diccionarioOrientaciones[tecla].lado2
                return True
            else:
                self.posicion = diccionarioOrientaciones[tecla].lado1
                return False
        return False

    def clonarLabebinto(self, tunel: Tunel) -> None:
        tunel.puedeClonarLaberinto()

    def atacar(self):
        self.juego.buscarBicho()


    def __str__(self):
        return self.nombre





