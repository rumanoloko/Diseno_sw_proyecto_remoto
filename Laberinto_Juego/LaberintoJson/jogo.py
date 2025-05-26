from Laberinto_Juego.Director import Director
from Laberinto_Juego.LaberintoBuilder import LaberintoBuilder

direc = Director()
direc.procesarArchivo(r"C:\Users\pasat\PycharmProjects\Diseño_sw_proyecto\Laberinto_Juego\LaberintoJson\lab3Hab.json")
print(direc.dict)

#direct procsar: ruta, 'laberinto2Hab.json'.
#direct.