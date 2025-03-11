import threading
import random
import time
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta
from Laberinto_Juego.BichoAgresivo import BichoAgresivo
from Laberinto_Juego.BichoPerezoso import BichoPerezoso
from Laberinto_Juego.Ente import Ente

class Bicho(Ente):
    def __init__(self, vidas: int = 5, modo=None, poder: int = 1, posicion: Habitacion = None) -> None:
        super().__init__(vidas, poder, posicion)
        self._modo = modo
        self._running = False
        self._timer = None  # Guardamos el temporizador para poder detenerlo

    def start_camina(self):
        """Inicia el movimiento del bicho cada 3 segundos sin bloquear el programa."""
        if not self._running:
            self._running = True
            self._mover_bicho()

    def stop_camina(self):
        """Detiene el movimiento del bicho."""
        self._running = False
        if self._timer:
            self._timer.cancel()  # Cancela el temporizador activo

    def _mover_bicho(self):
        """Ejecuta camina() y programa la siguiente ejecución en 3 segundos."""
        if self._running:
            self.camina()
            self._timer = threading.Timer(3, self._mover_bicho)  # Programa la siguiente ejecución
            self._timer.start()

    def camina(self):
        """El bicho intenta moverse a una habitación conectada."""
        if not self.posicion:
            print("Error: El bicho no tiene una posición inicial válida.")
            return

        opciones = [self.posicion.norte, self.posicion.oeste, self.posicion.este, self.posicion.sur]
        opciones = [o for o in opciones if o]  # Filtra valores None

        if not opciones:
            print("El bicho está atrapado y no puede moverse.")
            return

        neo_posicion = random.choice(opciones)
        print(f"La posición actual es {self.posicion}")

        if isinstance(neo_posicion, Pared):
            print("El bicho chocó con una pared")
        elif isinstance(neo_posicion, Puerta):
            if not neo_posicion.abierta:
                print("El bicho chocó contra una puerta cerrada")
            else:
                self.posicion = neo_posicion.lado2
                print(f"El bicho ahora está en {neo_posicion.lado2}")
        else:
            self.posicion = neo_posicion
            print(f"El bicho se ha movido a {self.posicion}")

    def iniAgresivo(self):
        self._modo = BichoAgresivo()
        self._poder = 10

    def iniPerezoso(self):
        self._modo = BichoPerezoso()
        self._poder = 1
