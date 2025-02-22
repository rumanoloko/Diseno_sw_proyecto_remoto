from ProductoHabitacion import ProductoHabitacion
from Builder import Builder


class BuilderHabitacion(Builder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        # Create a new instance of ProductoHabitacion
        self._producto = ProductoHabitacion()

    def producto(self) -> ProductoHabitacion:
        # Return the current product and reset for a new one
        producto = self._producto
        self.reset()
        return producto

    def añadirParedes(self):
        self._producto.add('pared')  # Add 'pared' to the product

    def añadirPuertas(self):
        self._producto.add('puerta')  # Add 'puerta' to the product

    def añadirCriaturas(self):
        self._producto.add('criatura')  # Add 'criatura' to the product

