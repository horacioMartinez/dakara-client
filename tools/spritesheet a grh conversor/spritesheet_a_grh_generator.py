# modifica los graficos.json para que apunten a los graficos de spritesheets con formato pixi en vez de a los graficos

# INSTRUCCIONES:
# en la misma carpeta deben estar graficos.json (los indices), y archivos nombre.json (spritesheet json). Se asume que hay un grafico con el mismo nombre de la spritesheet (el atlas)
# Itera a todos los archivos json y a partir de eso modifica graficos.json

import json
import struct
import os  
from pprint import pprint

graficosModificados = []

with open('graficos.json') as data_file:    
    graficos_data = json.load(data_file)

print("Generando graficos_resultantes.json\n")
for fn in os.listdir('.'):
	if not os.path.isfile(fn):
		continue
	if not fn.endswith(".json"):
		continue
	if fn == "graficos.json":
		continue
	if fn == "graficos_resultantes.json":
		continue
	nuevo_grafico_nombre = fn[0:fn.find('.')] #nombre de la imagen a la que apuntaran los graficos (el atlas) (idem nombre json sin extension)
	with open(fn) as atlas_file:    
		atlas = json.load(atlas_file)
		for atlas_grafico in atlas['frames']:
			atlas_grafico_number = int(atlas_grafico[0:atlas_grafico.find('.')]) #sacar .png y pasar a numero
			for grh in graficos_data:
				if type(grh) is not dict: #no es una lista (hay algunos que son 0)
					continue
				if 'grafico' not in grh:
					continue
				grh_grafico_number = grh['grafico']
				if atlas_grafico_number == grh_grafico_number:
					graficosModificados.append(grh_grafico_number)
					atlas_offX = atlas['frames'][atlas_grafico]['frame']['x']
					atlas_offY = atlas['frames'][atlas_grafico]['frame']['y']
					grh_offX = grh['offX']
					grh_offY = grh['offY']

					nuevo_offX = atlas_offX + grh_offX
					nuevo_offY = atlas_offY + grh_offY

					grh['offX'] = nuevo_offX
					grh['offY'] = nuevo_offY
					grh['css'] = grh['grafico']
					grh['grafico'] = nuevo_grafico_nombre



#Checkear que de los no modificados esten los png originales
graficosModificados.append(grh_grafico_number)
for grh in graficos_data:
	if type(grh) is not dict: #no es una lista (hay algunos que son 0)
		continue
	if 'grafico' not in grh:
		continue
	grh_grafico_number = grh['grafico']
	if grh_grafico_number in graficosModificados :
		continue
	if not os.path.isfile(str(grh_grafico_number) + '.png'):
		print( "ERRROR: " + str(grh_grafico_number))


destino = open("graficos_resultantes.json","w")
json.dump(graficos_data, destino, indent=2)