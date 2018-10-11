from pathlib import Path
from os import rename
import os
filearchivos=open("carpetas","r")


for i in filearchivos:
	nombre_carpeta=i.rstrip('\n')
#	print(nombre_carpeta)
	archivos=Path(nombre_carpeta).iterdir()
	counter=0
	for j in archivos:
		counter=counter+1
		rename(str(j), nombre_carpeta+"/"+nombre_carpeta+"_"+str(counter)+".jpg")
