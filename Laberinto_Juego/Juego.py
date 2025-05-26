from typing import TYPE_CHECKING
#from Laberinto_Juego.Ente import Bicho
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Contenedor import Contenedor
from Laberinto_Juego import Laberinto
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta

if TYPE_CHECKING:
    from Laberinto_Juego.Ente import Bicho

#from Laberinto_Juego.Laberinto import Laberinto

#from Laberinto_Juego.Director import Director
#from Laberinto_Juego.Creator import Creator


class Juego:
    #from Laberinto_Juego.Ente import Bicho
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []

    def crearLaberinto2Habitaciones(self) -> None:
        self.hab1 = Habitacion(1)
        self.hab2 = Habitacion(2)
        self.puerta = Puerta()
        self.hab1.norte = Pared()
        self.hab1.este = Pared()
        self.hab1.oeste = Pared()
        self.hab1.sur = self.puerta
        self.hab2.sur = Pared()
        self.hab2.este = Pared()
        self.hab2.oeste = Pared()
        self.hab2.norte = self.puerta
        self.puerta.lado1 = self.hab1
        self.puerta.lado2 = self.hab2

    def agregarPersonaje(self, nombre):
        from Laberinto_Juego.Ente import Personaje
        self.personaje = Personaje(nombre)


    def crearLaberinto2HabitacionesFM(self, unFM):
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        puerta = unFM.fabricarPuerta()
        puerta.abierta = True
        hab1.sur = puerta
        hab2.norte = puerta
        puerta.lado1 = hab1.sur
        puerta.lado2 = hab2.norte
        laberinto = Laberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        return laberinto

    def crearLaberinto4Hab4BichosFM(self, unFM = None) -> tuple():
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        hab3 = unFM.fabricarHabitacion(3)
        hab4 = unFM.fabricarHabitacion(4)
        puerta1 = unFM.fabricarPuerta()
        puerta2 = unFM.fabricarPuerta()
        puerta3 = unFM.fabricarPuerta()
        puerta4 = unFM.fabricarPuerta()
        bichoA1 = unFM.fabricarAgresivo(hab1)
        bichoA2 = unFM.fabricarAgresivo(hab2)
        bichoP1 = unFM.fabricarPerezoso(hab3)
        bichoP2 = unFM.fabricarPerezoso(hab3)

        bichoA1.posicion = hab1
        bichoA2.posicion = hab2
        bichoP1.posicion = hab3
        bichoP2.posicion = hab4

        puerta1.lado1 = hab1
        puerta1.lado2 = hab2
        hab1.este = puerta1
        hab2.oeste = puerta1

        puerta2.lado1 = hab2
        puerta2.lado2 = hab4
        hab2.sur = puerta2
        hab4.norte = puerta2

        puerta3.lado1 = hab4
        puerta3.lado2 = hab3
        hab4.oeste = puerta3
        hab3.este = puerta3

        puerta4.lado1 = hab3
        puerta4.lado2 = hab1
        hab3.norte= puerta4
        hab1.sur = puerta4

        laberinto = Laberinto()
        #laberinto.hijos = laberinto.hijos + [hab1, hab2, hab3, hab4]
        laberinto.añadirHijo(hab1)
        laberinto.añadirHijo(hab2)
        laberinto.añadirHijo(hab3)
        laberinto.añadirHijo(hab4)
        hab1.añadirHijo(bichoA1)
        hab2.añadirHijo(bichoA2)
        hab3.añadirHijo(bichoP1)
        hab4.añadirHijo(bichoP2)


        puerta1.abierta = True
        puerta2.abierta = True
        puerta3.abierta = True
        puerta4.abierta = True
        return laberinto, [bichoA1, bichoA2, bichoP1, bichoP2]


    def fabricarLaberinto(self):
        laberinto = Laberinto()
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        laberinto.hijos.append(hab1)
        laberinto.hijos.append(hab2)
        puerta = Puerta(True)
        hab1.sur = puerta
        hab2.norte = puerta
        return laberinto

    def obtenerHabitacionPorNumero(self):
        pass

    def buscarEnemigo(self):
        pass

    def buscarPersonaje(self, unBicho):
        pass
    #si posicionPersonaje == posicionBicho -> self person esAtacadoUnBicho:unBicho
    # juego crearLaberinto2HabitacionesFM: creator.
    #creatorB:= CreatorB.
    #juego := creatorB crearJuego
    #juego crearLaberinto2HabitacionesFM:creatorB
    #pared := creatorB fabricarPared
    #CreatorB sobreescribe el metodo de su clase padre crearPared
    #
    def gestionBichos(self):
        pass

    def agregarBicho(self, bicho) -> None:
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho) -> None:
        hayBicho = False
        if bicho in self.bichos:
            self.bichos.remove(bicho)
        else:
            pass
            #raise error


if __name__ == '__main__':
    from Laberinto_Juego.Ente import Personaje, Bicho
    from Laberinto_Juego.Creator import Creator
    juego = Juego()
    #ba = Bicho(5, BichoAgresivo, 5, None)
    #print(ba.esAgresivo())
    #print(ba.esPerezoso())
    creator = Creator()
    laber, bichos= juego.crearLaberinto4Hab4BichosFM(creator)
    print("Hola")
    print(laber)
    print(laber)
    for _ in bichos:
        print(_._modo)
        #print(_.esAgresivo())
        #print(_.esPerezoso())
        print(_.posicion)
    print("Laberinto")
    for hijo in laber.hijos:
        print(hijo)
    #print(laber.obtenerHabitacion(0).este)
    #print(laber.obtenerHabitacion(0).este.abierta)
    #print(laber.obtenerHabitacion(0).este.abierta)
    #print(laber.obtenerHabitacion(0).este)
    #print(laber.obtenerHabitacion(0).este.abierta)

    #print("\n\n\n")
    #print(laber.obtenerHabitacion(0).padre)
    #print(laber.obtenerHabitacion(1).padre)
    #print(laber.obtenerHabitacion(2).padre)
    #print(laber.obtenerHabitacion(3).padre)
    print()
    print("Iterador")
    print(laber.recorrer())
    juego.agregarPersonaje("Pepe")
    #print(bichos[0].posicion)
    #print(bichos[0].camina())
    bichos[0].start()
    bichos[1].start()
    bichos[2].start()
    bichos[3].start()
    #juego lanzarBichos.
    #juego acabarBichos.
    #juego agregarPersonaje:'Pepe'.
    #person:= juego person.
    #person irAlNorte.
    #person irAlSur.
    #person irAlEste.
    #person isAlOeste.
    #juego abrirPuertas.
    #juego cerrarPuertas.
    #juego lanzarBichos.
    #juego terminarBichos.





    #laber, vecBichos = x[0], x[1]
    #juego.bichos = juego.bichos+vecBichos


#hab orientaciones add:self fabricarNorte; add:self fabricarSur; add:self fabricarEste; add:self fabricarOeste
#hab orientaciones do[:each | hab ponerEnOr:each elemento: self fabricarPared].
#juego laberinto recorrer:[each | Trsnacript show:each printString; cr].
#juego laberinto recorrer:[each | each esPuerta ifTrue:[each abrir]].
#juego laberinto recorrer:[each | each esPuerta ifTrue:[each cerrar]].
#juego abrirPuertas. 'juego>>abrirPuerta
    #self laberinto abrirPuerta
#juego cerrarPuertas