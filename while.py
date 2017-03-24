'''Ciclo While'''
#while condicion:
#	codigo
#else:
#	codigo
contador = 0
while contador <= 10:
	print(contador)
	contador += 1 #Aumentar en 1 el contador
	if contador == 5:
		print("Estamos en el numero 5")
	if contador == 5:
		continue
	elif contador == 6:
		break
else: #Quiere decir que cuando termine de este mensaje
	print('El while a terminado')
contador = 0
bandera = True
while bandera:
	contador += 1
	if contador == 5:
		continue
	elif contador == 6:
		bandera = False
else: #Quiere decir que cuando termine de este mensaje
	print('El while a terminado')