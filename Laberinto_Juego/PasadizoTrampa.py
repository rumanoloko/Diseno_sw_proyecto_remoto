import threading
import time
from Laberinto_Juego import Ente
from Laberinto_Juego.Habitacion import Habitacion

class PasadizoTrampa(Habitacion):
    def __init__(self):
        super().__init__()
        self._estadoActivo = True
        self._poder = 4
        self._hilo_trampa = threading.Thread(target=self._detectar_entes, daemon=True)
        self._hilo_trampa.start()

    def _detectar_entes(self):
        while True:
            time.sleep(3)
            if self._estadoActivo:
                for hijo in self.hijos:
                    if isinstance(hijo, Ente):
                        hijo.esAtacadoPor(self)
                        print(f"[🔪 TRAMPA] {hijo} ha caído en la trampa del pasadizo.")

    @property
    def estadoActivo(self):
        return self._estadoActivo

    @estadoActivo.setter
    def estadoActivo(self, valor: bool):
        print(f"Trampa {'activada' if valor else 'desactiada'}")
        self._estadoActivo = valor

    def __str__(self):
        return "Pasadizo con trampas"
