from abc import ABC, abstractmethod

class Pared(ABC):
    def __init__(self):
        pass

    def __str__(self):
        return "Esta es una pared normal"

    def entrar(self):
        print("Orco, chocaste con una pared")
