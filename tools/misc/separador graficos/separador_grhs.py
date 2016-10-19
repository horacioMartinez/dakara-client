import json
import struct
import os  
from pprint import pprint

# separa los graficos que contienen varios grhs en graficos distintos.
# INSTRUCCIONES: poner esto, junto con graficos.json en la carpeta de los graficos. Tambien poner una carpeta "res"
# en res se crean todos los graficos separados y un nuevo graficos.json para ellos, los que pertenecen a animaciones estan separados por frams con _
with open('graficos.json') as data_file:    
    graficos_data = json.load(data_file)

graficos_procesados = {}

def getNumeroIndice (nombreGraf): #TODO: usar esto con las animaciones
	if nombreGraf not in graficos_procesados:
		graficos_procesados[nombreGraf] = 0
		return '_' + '%04d' % 0
	graficos_procesados[nombreGraf] = graficos_procesados[nombreGraf] + 1
	return '_' + '%04d' % graficos_procesados[nombreGraf]

id = 0

def getID():
	global id
	id = id +1
	return id

carpeta_destino = "res"

# Primero separo los de animaciones asi les pongo un indice a cada frame de la animacion

grhProcesados = []

for grh in graficos_data:
	if type(grh) is not dict: #no es una lista (hay algunos que son 0)
		continue
	if 'grafico' in grh: # es un grafico, quiero solo animaciones
		continue
	nuevo_graf_num = str(getID())
	for grhNumber in grh['frames']:

		if (grhNumber in grhProcesados):
			continue
		#pprint(grhNumber)
		grh = graficos_data[grhNumber]
		grhProcesados.append(grhNumber)

		grh_grafico_number = grh['grafico']
		grh_offX = grh['offX']
		grh_offY = grh['offY']
		grh_width = grh['width']
		grh_height = grh['height']

		nuevo_graf_frame_num = nuevo_graf_num + getNumeroIndice(nuevo_graf_num)
		nombre_archivo_destino = carpeta_destino + "/" + nuevo_graf_frame_num + '.png'

		#crea nuevos graficos
		os.system("convert " + str(grh_grafico_number) + ".png" + " -crop "+ str(grh_width) + "x" + str(grh_height) + "+" + str(grh_offX) + "+" + str(grh_offY) +" " + nombre_archivo_destino) 

		# cambiamos graficos.json
		graficos_data[grhNumber]['grafico'] = nuevo_graf_frame_num
		graficos_data[grhNumber]['offX'] = 0
		graficos_data[grhNumber]['offY'] = 0


for grh in graficos_data:
				if type(grh) is not dict: #no es una lista (hay algunos que son 0)
					continue
				if 'grafico' not in grh:
					continue
				if (grh['id'] in grhProcesados):
					continue

				grh_grafico_number = grh['grafico']
				grh_offX = grh['offX']
				grh_offY = grh['offY']
				grh_width = grh['width']
				grh_height = grh['height']

				nuevo_graf_num = str(getID())
				nombre_archivo_destino = carpeta_destino + "/" + nuevo_graf_num + '.png'

				#crea nuevos graficos
				os.system("convert " + str(grh_grafico_number) + ".png" + " -crop "+ str(grh_width) + "x" + str(grh_height) + "+" + str(grh_offX) + "+" + str(grh_offY) +" " + nombre_archivo_destino) 

				# cambiamos graficos.json
				grh['grafico'] = nuevo_graf_num
				grh['offX'] = 0
				grh['offY'] = 0

				'''
					nuevo_offX = atlas_offX + grh_offX
					nuevo_offY = atlas_offY + grh_offY

					grh['offX'] = nuevo_offX
					grh['offY'] = nuevo_offY
					grh['grafico'] = nuevo_grafico_nombre
					print (grh_grafico_number)
				'''

destino = open( carpeta_destino + "/" + "graficos_resultantes.json","w")
json.dump(graficos_data, destino, indent=2)

# ejemplo de cropear imagen:
# os.system("convert 3.png -crop 10x10+10+10 asd.png")





