try:
	#print(2/0)
	lista = [1,2]
	print(lista[9])
except Exception as ex:
	print(ex) 
	print("Ups... Hay un fallo")
finally:
	print("Se termino el script")
