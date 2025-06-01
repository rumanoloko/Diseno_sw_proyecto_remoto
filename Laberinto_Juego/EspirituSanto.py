import threading
import time
from Laberinto_Juego.Ente import Ente
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Juego import Juego

class EspirituSanto(Ente):
    def __init__(self, personajeCuidar: Ente, juego: Juego):
        super().__init__(nombre="Espíritu Santo", vidas=1, poder=0, posicion=None)
        self.objetivo = personajeCuidar
        self.juego = juego
        self._hilo = threading.Thread(target=self._vigilar, daemon=True)
        self._hilo.start()

    def _vigilar(self):
        while True:
            time.sleep(1)
            if self.objetivo.vidas <= 2:
                if self.objetivo.aura > 0:
                    print(f"[✨ Espíritu Santo] Nivel de vida crítica! Teletransportando a {self.objetivo.nombre}.")
                    posicion_segura = self.juego.obtenerPosicionSegura()
                    self.objetivo.posicion = posicion_segura
                    self.objetivo.vidas += self.objetivo.aura
                    self.objetivo.aura = 0
