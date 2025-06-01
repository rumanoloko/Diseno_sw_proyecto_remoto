from Laberinto_Juego.Director import Director
from Laberinto_Juego.Juego import Juego

if __name__ == '__main__':
    from Laberinto_Juego.Ente import Vivo
    director = Director()
    #juego = director.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab4hab4Bichos.json")
    juego = director.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab16Hab8Bichos.json")
    director.agregarPersonaje("Petru-Vlad Pasat", 10, 4, juego.HabitacionDePartida, juego, Vivo())
    juego.iniciarJuego(director)
    #hijos = juego.laberinto.hijos[5].hijos
    #for hijo in hijos:
    #    print(hijo)