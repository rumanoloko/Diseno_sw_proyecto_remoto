"""
import threading
import random
from typing import TYPE_CHECKING
from Laberinto_Juego import Habitacion, Pared, Puerta
from Laberinto_Juego import BichoAgresivo, BichoPerezoso, Ente
from Laberinto_Juego.Ente import Ente


class Bicho(Ente):
    _numero = 0
    _lock = threading.Lock()  # Lock global para sincronizar la salida

    def __init__(self, vidas: int = 5, modo=None, poder: int = 1, posicion: Habitacion = None) -> None:
        self._numero = Bicho._numero
        Bicho._numero += 1
        super().__init__(vidas, poder, posicion)
        self._modo = modo
        self._running = False
        self._timer = None  # Para manejar el temporizador

    def start(self):
        #Inicia la ejecución del Bicho solo si tiene una posición asignada.
        if self.posicion is None:
            with Bicho._lock:
                print(f"Error: No se puede iniciar {self} porque no tiene una posición asignada.")
            return

        with Bicho._lock:
            print(f"{self} ha comenzado en {self.posicion}")

        self.start_camina()

    def start_camina(self):
        #Inicia el movimiento del bicho cada 3 segundos sin bloquear el programa.
        if not self._running:
            self._running = True
            self._mover_bicho()

    def stop_camina(self):
        #Detiene el movimiento del bicho.
        self._running = False
        if self._timer:
            self._timer.cancel()  # Cancela el temporizador activo

    def _mover_bicho(self):
        #Ejecuta camina() y programa la siguiente ejecución en 3 segundos.
        if self._running:
            self.camina()
            self._timer = threading.Timer(3, self._mover_bicho)
            self._timer.start()

    def camina(self):
        #El bicho intenta moverse a una habitación conectada.
        if not self.posicion:
            with Bicho._lock:
                print(f"Error: {self} no tiene una posición inicial válida.")
            return

        opciones = [self.posicion.norte, self.posicion.oeste, self.posicion.este, self.posicion.sur]
        opciones = [o for o in opciones if o]  # Filtra valores None

        if not opciones:
            with Bicho._lock:
                print(f"{self} está atrapado y no puede moverse.")
            return

        neo_posicion = random.choice(opciones)

        with Bicho._lock:
            if isinstance(neo_posicion, Pared):
                print(f"El subnormal del {self} chocó con una pared")
            elif isinstance(neo_posicion, Puerta):
                if neo_posicion.abierta:
                    self.posicion = neo_posicion.lado2
                    print(f"{self} ahora está en {neo_posicion.lado2}")
                else:
                    print(f"{self} no puede avanzar por la puerta cerrada.")
            else:
                self.posicion = neo_posicion
                print(f"{self} se ha movido a {self.posicion}")

    def iniAgresivo(self):
        self._modo = BichoAgresivo()
        self._poder = 10

    def iniPerezoso(self):
        self._modo = BichoPerezoso()
        self._poder = 1

    def recorrer(self):
        with Bicho._lock:
            print(self)

    def __str__(self):
        return self._modo.__str__()
"""


