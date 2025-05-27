
from Laberinto_Juego.Director import Director
from Laberinto_Juego.LaberintoBuilder import LaberintoBuilder

direc = Director()
direc.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab4hab4Bichos.json")
x = direc.dict['laberinto']
print(len(x))
for y in x:
    print(y)

x = direc.dict['puertas']
print(len(x))
for y in x:
    print(y)

x = direc.dict['bichos']
print(len(x))
for y in x:
    print(y)

#direct procsar: ruta, 'laberinto2Hab.json'.
#direct.