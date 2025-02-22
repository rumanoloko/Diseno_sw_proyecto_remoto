from Builder import Builder
from BuilderHabitacion import BuilderHabitacion
class DirectorBuilder:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def contruccionHabitacionMinima(self) -> None:
        if not self.builder:
            raise ValueError("Builder is not set!")
        self.builder.añadirParedes()
        self.builder.añadirParedes()
        self.builder.añadirParedes()
        self.builder.añadirPuertas()
    def contruccionHabitacionMaxima(self) -> None:
        if not self.builder:
            raise ValueError("Builder is not set!")
        self.builder.añadirParedes()
        self.builder.añadirParedes()
        self.builder.añadirParedes()
        self.builder.añadirParedes()
        self.builder.añadirPuertas()
        self.builder.añadirPuertas()
        self.builder.añadirPuertas()
        self.builder.añadirPuertas()
        self.builder.añadirCriaturas()
