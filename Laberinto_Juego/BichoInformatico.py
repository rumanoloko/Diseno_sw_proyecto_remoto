from typing import override

from Laberinto_Juego.Modo import Modo

class BichoInformatico(Modo):
    _numero = 0

    def __init__(self):
        super().__init__()
        self._numero = BichoInformatico._numero
        BichoInformatico._numero += 1

    def __str__(self):
        return f"Bicho informático {self._numero}"

    @override
    def esInformatico(self) -> bool:
        return True

    def duerme(self):
        return "Los informatico no duermen sobre todo cuando hay test de API"

    def atacar(self, objetivo):
        print("Pregunta informática antes de decidir atacar:")
        print("¿Quién es el creador de xTreme Programming?")
        print("1. Kent Beck")
        print("2. John Cena")
        print("3. El profesor de API")
        print("4. Bob Esponja")

        respuesta = input("Tu respuesta (1-4): ").strip()


        if respuesta == "1":
            print("La verdad ni yo me acuerdo de la respuesta pero me suena esa como la buena")
        else:
            print("Por favor......Kent Beck es la clave")
            objetivo.esAtacadoPor(self)

    def __str__(self):
        return "Soy un bicho que solo ataca a los que no saben reponder mi pregunta"
