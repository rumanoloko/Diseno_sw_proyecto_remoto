from Laberinto_Juego.Forma import Coordenada2D


class Gui:
    def __init__(self):
        self.exist = True
        self.dict = None
    def mostrar_laberinto(self, laberinto, posicion_actual: Coordenada2D):
        if laberinto and self.dict == None:
            self.dict = laberinto
        filas, columnas = self.obtener_dimensiones(laberinto)

        # Crear matriz con habitaciones representadas por "□"
        matriz = [["□" for _ in range(columnas)] for _ in range(filas)]

        # Marcar la posición actual en rojo
        x, y = posicion_actual
        matriz[x][y] = "\033[31mx\033[0m"  # Código ANSI para color rojo

        # Imprimir la matriz del laberinto
        for fila in matriz:
            print("  ".join(fila))

    def obtener_dimensiones(self, laberinto):
        maxX, maxY = 0, 0
        habitaciones = laberinto['laberinto']
        for hab in habitaciones:
            maxX, maxY = max(maxX, hab['num'][0]), max(maxX, hab['num'][1])
            #print(hab['num'])
        #print(maxX + 1, " ", maxY + 1)
        return maxX + 1, maxY + 1
        #filas = max(hab[][0] for hab in laberinto) + 1
        #columnas = max(hab["num"][1] for hab in laberinto) + 1
        #return filas, columnas