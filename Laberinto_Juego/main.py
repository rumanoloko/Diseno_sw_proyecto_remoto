from Laberinto_Juego.Director import Director
from Laberinto_Juego.Juego import Juego

if __name__ == '__main__':
    from Laberinto_Juego.Ente import Vivo
    director = Director()
    #juego = director.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab4hab4Bichos.json")
    juego = director.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab16Hab8Bichos.json")
    director.agregarPersonaje("Petru-Vlad Pasat", 10, 4, juego.HabitacionDePartida, juego, Vivo())
    #print(juego.laberinto.hijos[0])
    #print(juego.bichos[0])
    #print(juego.personaje)
    #print(juego.iniciarJuego(director.dict))
    juego.iniciarJuego(director)
    #hijos = juego.laberinto.hijos[5].hijos
    #for hijo in hijos:
    #    print(hijo)
    print("main2")
    for habitacion in juego.laberinto.hijos:
        for h in habitacion.hijos:
            print(h)