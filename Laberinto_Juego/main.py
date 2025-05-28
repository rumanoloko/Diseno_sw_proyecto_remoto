from Laberinto_Juego.Juego import Juego

if __name__ == '__main__':
    from Laberinto_Juego.Ente import Personaje, Bicho
    from Laberinto_Juego.Creator import Creator
    juego = Juego()
    creator = Creator()
    laber, bichos = juego.crearLaberinto4Hab4BichosFM(creator)
    #for hijo in laber.hijos:
        #print(hijo)
    laber.recorrer(print)
    juego.agregarPersonaje("Pepe")

    bichos[0].start()
    #bichos[1].start()
    #bichos[2].start()
    #bichos[3].start()
    juego.laberinto.recorrer(print)
    print(juego.laberinto.hijos)