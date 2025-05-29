#from Laberinto_Juego.Juego import Juego
import copy
from sys import exception

from Laberinto_Juego.BichoAgresivo import BichoAgresivo
from Laberinto_Juego.BichoPerezoso import BichoPerezoso
from Laberinto_Juego.Ente import Bicho
from Laberinto_Juego.Forma import Cuadrado
from Laberinto_Juego.Gui import Gui
from Laberinto_Juego.Habitacion import Habitacion
from Laberinto_Juego.Juego import Juego
from Laberinto_Juego.Laberinto import Laberinto
from Laberinto_Juego.Orientacion import Orientacion, Norte, Sur, Este, Oeste
from Laberinto_Juego.Pared import Pared
from Laberinto_Juego.Puerta import Puerta
from Laberinto_Juego.Tunel import Tunel


class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego = None

    def fabricarJuego(self, diccionario):
        self.juego = Juego()
        self.juego.laberinto, self.juego.bichos = self.fabricarLaberinto(diccionario)
        self.fabricarGui()
        #self.juego.prototipo = self.laberinto
        #self.juego.laberinto = copy.deepcopy(self.juego.prototipo)
        #for bicho in self.juego.bichos:
            #bicho.start()
        return self.juego

    def fabricarGui(self):
        self.juego.gui = Gui()

    def fabricarLaberinto(self, diccionario):
        habitaciones, puertas, bichos = {},[],[]

        for habitacion in diccionario['laberinto']:
            hab = self.fabricarHabitacion(habitacion['num'])
            habitaciones[tuple(habitacion['num'])] = hab

        for bicho in diccionario['bichos']:
            bich = self.fabricarBicho(bicho['modo'], bicho['posicion'])
            #print("Habitacion a asignar al bicho", habitaciones[tuple(bicho['posicion'])])
            #print("Bicho creado", bich)
            bich.posicion = habitaciones[tuple(bicho['posicion'])]
            print('\n\n')
            print(f"{bich} esta en la habitacion {bich.posicion.numero}")
            print(f"Y la habitacion {bich.posicion.numero} en la que se encuentra contiene:")
            habitaciones[tuple(bicho['posicion'])].añadirHijo(bich)
            for contenido in habitaciones[tuple(bicho['posicion'])].hijos:
                print(contenido)
            bichos.append(bich)

        for puerta in diccionario['puertas']:
            #print("IMPRIMIENDO PUERTA: => ",puerta)
            porta = self.fabricarPuerta()
            porta.lado1 = habitaciones[tuple(puerta['lado1'])]
            porta.lado2 = habitaciones[tuple(puerta['lado2'])]
            porta.abierta = puerta['abierta']
            habitaciones[tuple(puerta['lado1'])].añadir(puerta['direccion1'], porta)
            habitaciones[tuple(puerta['lado2'])].añadir(puerta['direccion2'], porta)
            #porta.abierta = True
            puertas.append(porta)

        """
        print("\n\n\n\n\n")
        for kay, value in habitaciones.items():
            print(f"Habitacion {value.numero}")
            print(value.sur)
            print(value.norte)
            print(value.este)
            print(value.oeste)
            print("\n\n\n")
        """
        laberinto = Laberinto()
        for key, value in habitaciones.items():
            laberinto.añadirHijo(value)

        return laberinto, bichos

    """
    def fabricarHabitacion(self, num):
        hab = Habitacion(num)
        hab.forma = self.fabricarForma()
        hab.forma.num = num
        # hab.agregarOrientacion(self.fabricarNorte())
        # hab.agregarOrientacion(self.fabricarSur())
        # hab.agregarOrientacion(self.fabricarEste())
        # hab.agregarOrientacion(self.fabricarOeste())
        for each in hab.forma.orientaciones:
            hab.ponerElementoEnOrientacion(self.fabricarPared(), each)
        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1, o1, lado2, o2):
        hab1 = self.laberinto.obtenerHabitacion(lado1)
        hab2 = self.laberinto.obtenerHabitacion(lado2)
        puerta = Puerta(hab1, hab2)
        objOr1 = self.obtenerObjeto(o1)
        objOr2 = self.obtenerObjeto(o2)
        hab1.ponerElementoEnOrientacion(puerta, objOr1)
        hab2.ponerElementoEnOrientacion(puerta, objOr2)

    def obtenerObjeto(self, cadena):
        obj = None
        match cadena:
            case 'Norte':
                obj = self.fabricarNorte()
            case 'Sur':
                obj = self.fabricarSur()
            case 'Este':
                obj = self.fabricarEste()
            case 'Oeste':
                obj = self.fabricarOeste()
        return obj

    def fabricarForma(self):
        forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma
    """
    def fabricarHabitacion(self, numeroHabitacion: int) -> Habitacion:
        habitacion = Habitacion(numeroHabitacion)
        habitacion.forma = self.fabricarFormaCuadrada()
        paredNorte = self.fabricarPared()
        paredSur = self.fabricarPared()
        paredEste = self.fabricarPared()
        paredOeste = self.fabricarPared()
        habitacion.ponerElementoEnOrientacion(paredNorte, Norte())
        habitacion.ponerElementoEnOrientacion(paredSur, Sur())
        habitacion.ponerElementoEnOrientacion(paredEste, Este())
        habitacion.ponerElementoEnOrientacion(paredOeste, Oeste())


        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        return habitacion

    def fabricarFormaCuadrada(self):
        forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma

    def fabricarPuerta(self) -> Puerta:
        return Puerta()

    def fabricarPared(self) -> Pared:
        return Pared()

    def fabricarAgresivo(self, habitacion: Habitacion)-> Bicho:
        bicho = Bicho()
        bicho.iniAgresivo()
        bicho.posicion = habitacion
        return bicho

    def fabricarPerezoso(self, habitacion: Habitacion)-> Bicho:
        bicho = Bicho()
        bicho.iniPerezoso()
        bicho.posicion = habitacion
        return bicho

    def fabricarNorte(self) -> Orientacion:
        return Norte()

    def fabricarSur(self) -> Orientacion:
        return Sur()

    def fabricarEste(self) -> Orientacion:
        return Este()

    def fabricarOeste(self) -> Orientacion:
        return Oeste()

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        #bicho.modo = BichoAgresivo()
        bicho.iniAgresivo()
        return bicho

    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        #bicho.modo = BichoPerezoso()
        bicho.iniPerezoso()
        return bicho

    def obtenerJuego(self):
        return self.juego

    def fabricarTunelEn(self, unCont):
        tunel = Tunel(None)
        unCont.agregar_hijo(tunel)

    def fabricarBicho(self, modo, posicion) -> Bicho:
        bicho = Bicho()
        if modo == 'BichoAgresivo':
            bicho.iniAgresivo()
        elif modo == 'BichoPerezoso':
            bicho.iniPerezoso()
        else:
            raise exception("Se paso un string de moto de bicho que no existe")
        #hab = self.laberinto.obtenerHabitacion(posicion)
        #hab.entrar(bicho)
        #bicho.posicion = hab
        #self.juego.agregar_bicho(bicho)
        return bicho



