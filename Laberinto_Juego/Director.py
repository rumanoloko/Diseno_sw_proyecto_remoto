import json
from Laberinto_Juego.LaberintoBuilder import LaberintoBuilder
class Director:
    def __init__(self):
        self.builder = LaberintoBuilder()
        self.dict = {}

    def procesarArchivo(self, archivoJson):
        self.leerArchivo(archivoJson)
        self.iniBuilder
        self.fabricarLaberinto
        self.fabricarJuego
        self.fabricarBicho

    def leerArchivo(self, archivoJson):
        try:
            # Abrir el archivo JSON y cargar su contenido en self.dict
            with open(archivoJson, 'r', encoding='utf-8') as file:
                self.dict = json.load(file)
        except FileNotFoundError:
            print(f"El archivo {archivoJson} no se encontró.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON {archivoJson}.")

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto

        #(self dict at:'laberinto') do:[:each | self fabricarLaberintoRecursivo:each en:'root'].
        #(self dict at:'puertas' do:[each |
        #        self.builder fabricarPuertasL1:(each at:1) or1:(each at:2) n2:(each at:3) or2:(each at:4)].

    def fabricarFaberintoRecursivo(self): #fabricarLaberintoRecursivo:unDic en:padre
        #(unDir at:'tipo')='habitacion' ifTrue:
        pass

    def fabricarHabitacion(self, unNum):
        habitacion = None

    def fabricarNorte(self):
        pass

    def fabricarEste(self):
        pass

    def fabricarOeste(self):
        pass

    def fabricarPared(self):
        pass

    def iniBuilder(self):
        pass

    def fabricarJuego(self):
        pass

    def fabricarBicho(self):
        #(self)
        pass



    def __str__(self):
        return "El director procesa el fichero.json y aparte se encarga del proceso de creación."
