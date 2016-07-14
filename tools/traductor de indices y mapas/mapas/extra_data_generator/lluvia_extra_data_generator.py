import json
import struct
import os  
origen = open("./FK.ind", "rb")
destino = open("./extra_data","w")

origen.read(256 + 7)  # saco header

def escribirMapaData (mapa,lluvia):
	destino.write('"' + str(mapa) + '"' +":")
	destino.write('{')
	destino.write('"outdoor"'+":"+str(lluvia))
	destino.write('}')

cantidad_mapas = struct.unpack('<H', (origen.read(2)))[0] # l1

destino.write('{')
x = 1
while (x < cantidad_mapas +1):
	# numero X = numero de mapa
	lluvia = struct.unpack('<B', (origen.read(1)))[0]
	if (lluvia > 0):
		lluvia = 1
	escribirMapaData(x,lluvia);
	destino.write(',')
	x = x +1

#Hay algunos mapas que no figura en FK.ind, lleno con mas mapas y los pongo en 0
extra = 100
while (x < cantidad_mapas +extra):
	escribirMapaData(x,0);
	destino.write(',')
	x = x +1

#ultimo paso sin ,
escribirMapaData(x,0);

destino.write('}')
destino.close()
