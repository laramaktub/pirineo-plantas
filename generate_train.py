from pathlib import Path
from os import rename
import os
filearchivos=open("carpetas","r")

counter=0
for i in filearchivos:
	nombre_carpeta=i.rstrip('\n')
#	print(nombre_carpeta)
	archivos=Path(nombre_carpeta).iterdir()
	
	for j in archivos:
		print(str(j)+ " " + str(counter))
	counter=counter+1
