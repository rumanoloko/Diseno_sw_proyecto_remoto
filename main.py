from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys


class Habitacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habitación con Paredes Definidas")
        self.setGeometry(200, 200, 450, 450)

        # Dimensiones de la habitación (6x6)
        self.filas, self.columnas = 7,7
        self.posicion_x, self.posicion_y = 2, 2  # Posición inicial del personaje

        # Crear widget central y el layout en cuadrícula
        self.central_widget = QWidget(self)
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(0)  # Sin espacios entre celdas
        self.setCentralWidget(self.central_widget)

        # Dibujar la habitación con paredes y salidas
        self.dibujar_habitacion()

    def dibujar_habitacion(self):
        # Limpiar el grid layout
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

                if [x, y] == [0,3] or [x, y] == [6,3] or [x, y] == [3,0] or [x, y] == [3,6]:
                    contenido = " "

                label = QLabel(contenido)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet("font-size: 35px; font-family: Courier;")  # Fuente monoespaciada
                self.grid_layout.addWidget(label, x, y)

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

        self.posicion_x, self.posicion_y = nueva_x, nueva_y
        self.dibujar_habitacion()


# Ejecutar la aplicación
app = QApplication(sys.argv)
ventana = Habitacion()
ventana.show()
sys.exit(app.exec())
