import string
import threading
import random
from typing import override, TYPE_CHECKING
from Laberinto_Juego import Habitacion, Puerta
#from Laberinto_Juego.EstadoEnte  import EstadoEnte
from Laberinto_Juego.BichoAgresivo import BichoAgresivo
from Laberinto_Juego.BichoPerezoso import BichoPerezoso
from Laberinto_Juego import Tunel
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta

class EstadoEnte:
    def __init__(self)  -> None:
        pass


    def vivir(self, ente) -> None:
        pass

    def morir(self, ente) -> None:
        pass


class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()


    def vivir(self,ente) -> None:
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

    def esAtacadoPor(self, atacante):
        print(f"{self} es atacado por {atacante}")
        self._vidas -= atacante.poder
        print(f"A {self} le quedan {self._vidas}")

        if self._vidas <= 0:
            print(f"{self} a muerto")
            self.estadoEnte.morir(self)

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


class Bicho(Ente):
    _numero = 0
    _lock = threading.Lock()  # Lock global para sincronizar la salida
    def __init__(self, modo=None, posicion: Habitacion = None, vidas: int = 5, poder: int = 1) -> None:
        super().__init__(vidas, poder, posicion)
        self._numero = Bicho._numero
        Bicho._numero += 1
        self._modo = modo
        self._running = False
        self._timer = None  # Para manejar el temporizador

    def start(self):
        """Inicia la ejecución del Bicho solo si tiene una posición asignada."""
        if self._posicion is None:
            with Bicho._lock:
                print(f"Error: No se puede iniciar {self} porque no tiene una posición asignada.")
            return

        with Bicho._lock:
            print(f"{self} ha comenzado en {self.posicion}")

        self.start_camina()

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
            self._timer = threading.Timer(3, self._mover_bicho)
            self._timer.start()

    def camina(self):
        """El bicho intenta moverse a una habitación conectada."""
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

    def iniAgresivo(self):
        self._modo = BichoAgresivo()
        self._poder = 10

    def iniPerezoso(self):
        self._modo = BichoPerezoso()
        self._poder = 1

    def recorrer(self, func):
        with Bicho._lock:
            func(self)

    def __str__(self):
        return self._modo.__str__()

class Personaje(Ente):
    from Laberinto_Juego.Juego import Juego
    def __init__(self, nombre: string, vidas: int = 10, poder: int = 4, posicion:Habitacion = None, juego:Juego = None, estadoEnte: EstadoEnte = Vivo()) -> None:
        super().__init__(vidas, poder, posicion, juego, estadoEnte)
        self._nombre = nombre

    def clonarLabeinto(self, tunel: Tunel) -> None:
        tunel.puedeClonarLaberinto()

    def atacar(self):
        self.juego.buscarBicho()

    def __str__(self):
        return self._nombre

    def start(self):
        print("Here we go again")


