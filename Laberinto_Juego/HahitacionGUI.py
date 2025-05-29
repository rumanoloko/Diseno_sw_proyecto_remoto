from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys

from Laberinto_Juego import Pared, Puerta


class HabitacionGUI(QMainWindow,):
    def __init__(self, juego):
        super().__init__()
        self.setWindowTitle("Habitación con Paredes Definidas")
        self.setGeometry(200, 200, 450, 450)
        self.juego = juego
        self.diccionarioSalidas = {
            'Norte': None,
            'Sur': None,
            'Este': None,
            'Oeste': None
        }
        # Dimensiones de la habitación (6x6)
        self.filas, self.columnas = 7,7
        self.posicion_x, self.posicion_y = 3,3  # Posición inicial del personaje

        # Crear widget central y el layout en cuadrícula
        self.central_widget = QWidget(self)
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(0)  # Sin espacios entre celdas
        self.setCentralWidget(self.central_widget)

        # Dibujar la habitación con paredes y salidas
        self.dibujar_habitacion()

    def dibujar_habitacion(self):
        # Limpiar el grid layout
        self.analizarHabitacion()
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        # Generar la estructura de la habitación
        for x in range(self.filas):
            for y in range(self.columnas):
                # Definir los elementos visuales
                if (x == 0 and y == 0):
                    contenido = "╔"  # Esquina superior izquierda
                elif (x == 0 and y == self.columnas - 1):
                    contenido = "╗"  # Esquina superior derecha
                elif (x == self.filas - 1 and y == 0):
                    contenido = "╚"  # Esquina inferior izquierda
                elif (x == self.filas - 1 and y == self.columnas - 1):
                    contenido = "╝"  # Esquina inferior derecha
                elif x == 0 or x == self.filas - 1:
                    contenido = "═"  # Pared horizontal
                elif y == 0 or y == self.columnas - 1:
                    contenido = "║"  # Pared vertical
                elif (x == 0 and y == self.columnas // 2) or (x == self.filas - 1 and y == self.columnas // 2):
                    contenido = "▲" if x == 0 else "▼"  # Puerta superior/inferior
                elif (y == 0 and x == self.filas // 2) or (y == self.columnas - 1 and x == self.filas // 2):
                    contenido = "◄" if y == 0 else "►"  # Puerta izquierda/derecha
                else:
                    contenido = " "  # Espacio vacío dentro de la habitación

                # Mostrar el personaje en el centro
                if [x, y] == [self.posicion_x, self.posicion_y]:
                    contenido = "🧍"

                if [x, y] == [0,3]: #NORTE
                    contenido = self.diccionarioSalidas['Norte']
                if[x, y] == [6,3]: #SUR
                    contenido = self.diccionarioSalidas['Sur']
                if [x, y] == [3,0]: #OESTE
                    contenido = self.diccionarioSalidas['Oeste']
                if [x, y] == [3,6]: #ESTE
                    contenido = self.diccionarioSalidas['Este']


                label = QLabel(contenido)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet("font-size: 35px; font-family: Courier;")  # Fuente monoespaciada
                self.grid_layout.addWidget(label, x, y)

    def analizarHabitacion(self):
        habitacion = self.juego.personaje.posicion
        """
        # Debug: Mostrar información de la habitación
        print("Clase Norte:", habitacion.norte.__class__.__name__)
        print("Clase Sur:", habitacion.sur.__class__.__name__)
        print("Clase Este:", habitacion.este.__class__.__name__)
        print("Clase Oeste:", habitacion.oeste.__class__.__name__)
        """
        # Norte
        if habitacion.norte.__class__.__name__ == 'Pared':
            self.diccionarioSalidas['Norte'] = '═'
        elif habitacion.norte.__class__.__name__ == 'Puerta' and habitacion.norte.abierta:
            self.diccionarioSalidas['Norte'] = ' '
        else:
            self.diccionarioSalidas['Norte'] = '🟫'

        # Sur
        if habitacion.sur.__class__.__name__ == 'Pared':
            self.diccionarioSalidas['Sur'] = '═'
        elif habitacion.sur.__class__.__name__ == 'Puerta' and habitacion.sur.abierta:
            self.diccionarioSalidas['Sur'] = ' '
        else:
            self.diccionarioSalidas['Sur'] = '🟫'

        # Este
        if habitacion.este.__class__.__name__ == 'Pared':
            self.diccionarioSalidas['Este'] = '║'
        elif habitacion.este.__class__.__name__ == 'Puerta' and habitacion.este.abierta:
            self.diccionarioSalidas['Este'] = ' '
        else:
            self.diccionarioSalidas['Este'] = '🟫'

        # Oeste
        if habitacion.oeste.__class__.__name__ == 'Pared':
            self.diccionarioSalidas['Oeste'] = '║'
        elif habitacion.oeste.__class__.__name__ == 'Puerta' and habitacion.oeste.abierta:
            self.diccionarioSalidas['Oeste'] = ' '
        else:
            self.diccionarioSalidas['Oeste'] = '🟫'

    def keyPressEvent(self, event: QKeyEvent):
        nueva_x, nueva_y = self.posicion_x, self.posicion_y

        if event.key() == Qt.Key.Key_Up and nueva_x > 1:
            nueva_x -= 1
        elif event.key() == Qt.Key.Key_Down and nueva_x < self.filas - 2:
            nueva_x += 1
        elif event.key() == Qt.Key.Key_Left and nueva_y > 1:
            nueva_y -= 1
        elif event.key() == Qt.Key.Key_Right and nueva_y < self.columnas - 2:
            nueva_y += 1
        elif event.key() == Qt.Key.Key_Up and nueva_x  == 1 and nueva_y == 3 and self.diccionarioSalidas['Norte'] == ' ':
            nueva_x = 5
            if self.juego.personaje.posicion.numero == self.juego.personaje.posicion.norte.lado1.numero:
                self.juego.personaje.posicion = self.juego.personaje.posicion.norte.lado2
            else:
                self.juego.personaje.posicion = self.juego.personaje.posicion.norte.lado1
        elif event.key() == Qt.Key.Key_Down and nueva_x == 5 and nueva_y == 3 and self.diccionarioSalidas['Sur'] == ' ':
            nueva_x = 1
            if self.juego.personaje.posicion.numero == self.juego.personaje.posicion.sur.lado1.numero:
                self.juego.personaje.posicion = self.juego.personaje.posicion.sur.lado2
            else:
                self.juego.personaje.posicion = self.juego.personaje.posicion.sur.lado1

        elif event.key() == Qt.Key.Key_Left and nueva_y == 1 and nueva_x == 3 and self.diccionarioSalidas['Oeste'] == ' ':
            nueva_y = 5
            if self.juego.personaje.posicion.numero == self.juego.personaje.posicion.oeste.lado1.numero:
                self.juego.personaje.posicion = self.juego.personaje.posicion.oeste.lado2
            else:
                self.juego.personaje.posicion = self.juego.personaje.posicion.oeste.lado1
        elif event.key() == Qt.Key.Key_Right and nueva_y == 5 and nueva_x == 3 and self.diccionarioSalidas['Este'] == ' ':
            nueva_y = 1
            if self.juego.personaje.posicion.numero == self.juego.personaje.posicion.este.lado1.numero:
                self.juego.personaje.posicion = self.juego.personaje.posicion.este.lado2
            else:
                self.juego.personaje.posicion = self.juego.personaje.posicion.este.lado1

        self.posicion_x, self.posicion_y = nueva_x, nueva_y
        print(self.posicion_x, " ", self.posicion_y)
        #print(type(self.juego.personaje.posicion.sur))
        #self.analizarHabitacion()
        self.dibujar_habitacion()