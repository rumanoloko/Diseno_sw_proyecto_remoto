from Laberinto_Juego.Bicho import Bicho
from Laberinto_Juego.Creator import  Creator
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Laberinto import Laberinto
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta

class Juego:

    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = [Bicho()]

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

    def crearLaberinto2HabitacionesFM(self, unFM:Creator) -> Laberinto:
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        puerta = unFM.fabricarPuerta()
        puerta.abierta = True
        hab1.sur = puerta
        hab2.norte = puerta
        puerta.lado1 = hab1.sur
        puerta.lado2 = hab2.norte
        laberinto = Laberinto()
        laberinto.append(hab1)
        laberinto.append(hab2)
        return laberinto

    def crearLaberinto4Hab4BichosFM(self, unFM:Creator) -> tuple():
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        hab3 = unFM.fabricarHabitacion(3)
        hab4 = unFM.fabricarHabitacion(4)
        puerta1 = unFM.fabricarPuerta()
        puerta2 = unFM.fabricarPuerta()
        puerta3 = unFM.fabricarPuerta()
        puerta4 = unFM.fabricarPuerta()
        bichoA1 = unFM.fabricarAgresivo()
        bichoA2 = unFM.fabricarAgresivo()
        bichoP1 = unFM.fabricarPerezoso()
        bichoP2 = unFM.fabricarPerezoso()

        bichoA1.posicion = hab1
        bichoA2.posicion = hab2
        bichoP1.posicion = hab3
        bichoP2.posicion = hab4

        puerta1.lado1 = hab1
        puerta1.lado2 = hab2
        hab1.este = puerta1
        hab2.oeste = puerta2

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
        laberinto.habitaciones = laberinto.habitaciones + [hab1, hab2, hab3, hab4]

        puerta1.abierta = False
        puerta2.abierta = True
        puerta3.abierta = True
        puerta4.abierta = True
        return (laberinto, [bichoA1, bichoA2, bichoP1, bichoP2])


    def fabricarLaberinto(self) -> Laberinto:
        laberinto = Laberinto()
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        laberinto.habitaciones.append(hab1)
        laberinto.habitaciones.append(hab2)
        puerta = Puerta(True)
        hab1.sur = puerta
        hab2.norte = puerta
        return laberinto

    def obtenerHabitacionPorNumero(self):
        pass
# juego crearLaberinto2HabitacionesFM: creator.
#creatorB:= CreatorB.
#juego := creatorB crearJuego
#juego crearLaberinto2HabitacionesFM:creatorB
#pared := creatorB fabricarPared
#CreatorB sobreescribe el metodo de su clase padre crearPared
#
    def gestionBichos(self):
        pass

    def agregarBicho(self, bicho:Bicho) -> None:
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho:Bicho) -> None:
        hayBicho = False
        if bicho in self.bichos:
            self.bichos.remove(bicho)
        else:
            pass
            #raise error


if __name__ == '__main__':
    juego = Juego()
    #ba = Bicho(5, BichoAgresivo, 5, None)
    #print(ba.esAgresivo())
    #print(ba.esPerezoso())
    creator = Creator()
    laber, bichos = juego.crearLaberinto4Hab4BichosFM(creator)
    print(laber)
    for _ in bichos:
        print(_)
        #print(_.esAgresivo())
        #print(_.esPerezoso())
        #print(_.posicion)
        #print(_._modo)
    print(laber.habitaciones[0].este)
    print(laber.habitaciones[0].este.abierta)
    print(laber.habitaciones[0].este.abierta)
    print(laber.habitaciones[0].este)
    print(laber.habitaciones[0].este.abierta)

    #laber, vecBichos = x[0], x[1]
    #juego.bichos = juego.bichos+vecBichos





