class ProductoHabitacion:
    def __init__(self) -> None:
        self.componentes = []

    def añadirComponente(self, componente:any) -> None:
        self.componentes.append(componente)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.componentes)}", end="")