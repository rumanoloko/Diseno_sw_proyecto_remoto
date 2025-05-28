import json
from typing import Any

from Laberinto_Juego.LaberintoBuilder import LaberintoBuilder

class Director:
    def __init__(self):
        self.builder = LaberintoBuilder()
        self.dict = {'Diccionario': 'Vacio'}
        self.juego = None
    def procesarArchivo(self, archivoJson):
        self.leerArchivo(archivoJson)
        #self.fabricarLaberinto()
        self.juego = self.fabricarJuego()
        #self.juego.bichos[0].start()
        #self.fabricarBicho()
        return self.juego

    def leerArchivo(self, archivoJson) -> Any:
        try:
            # Abrir el archivo JSON y cargar su contenido en self.dict
            with open(archivoJson, 'r', encoding='utf-8') as file:
                self.dict = json.load(file)
        except FileNotFoundError:
            print(f"El archivo {archivoJson} no se encontró.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON {archivoJson}.")

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto(self.dict)

    def fabricarJuego(self):
        return self.builder.fabricarJuego(self.dict)

    def fabricarBicho(self):
        return self.builder.fabricarBicho(self.dict)

    def fabricarLaberintoRecursivo(self, each, padre): #fabricarLaberintoRecursivo:unDic en:padre
        #(unDir at:'tipo')='habitacion' ifTrue:
        print(each)
        if each['tipo']=='habitacion':
            con=self.builder.fabricarHabitacion(each['num'])
        if each['tipo']=='tunel':
            self.builder.fabricarTunelEn(padre)
        if 'hijos'in each.keys():
            for cadaUno in each['hijos']:
                self.fabricarLaberintoRecursivo(cadaUno,con)

    def __str__(self):
        return "Soy el director que procesa el fichero Json y aparte se encarga del proceso de creación."
