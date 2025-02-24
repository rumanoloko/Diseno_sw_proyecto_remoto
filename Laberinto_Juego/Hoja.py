from Laberinto_Juego.ElementoMapa import ElementoMapa


class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Esto es una hoja"