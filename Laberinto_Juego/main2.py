from Laberinto_Juego.Director import Director
from Laberinto_Juego.Juego import Juego

if __name__ == '__main__':
    director = Director()
    #juego = director.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab4hab4Bichos.json")
    juego = director.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab16Hab8Bichos.json")
    juego.agregarPersonaje("Pepe")
    juego.laberinto.hijos[0].start
    #juego.laberinto.recorrer(print)
    #print(juego.laberinto.hijos)