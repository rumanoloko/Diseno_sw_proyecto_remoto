from typing import override
from abc import abstractmethod

class Orientacion:
    def __init__(self, numero):
        pass

    def __str__(self):
        return "Esto es una horientacion"

    @abstractmethod
    def crearOrientacion(self):
        pass

class Norte(Orientacion):
    def __init__(self):
        super().__init__()
    @override
    def __str__(self):
        return "Esto es la horientacion norte"

    @override
    def crearOrientacion(self):
        return Norte()

class Sur(Orientacion):
    def __init__(self):
        super().__init__()
    @override
    def __str__(self):
        return "Esto es la horientacion sur"

    @override
    def crearOrientacion(self):
        return Sur()

class Este(Orientacion):
    def __init__(self):
        super().__init__()
    @override
    def __str__(self):
        return "Esto es la horientacion este"

    @override
    def crearOrientacion(self):
        return Este()

class Oeste(Orientacion):
    def __init__(self):
        super().__init__()
    @override
    def __str__(self):
        return "Esto es la horientacion oeste"

    @override
    def crearOrientacion(self):
        return Oeste()