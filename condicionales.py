fruta = 'Manzana'
''' if condicion :
		codigo
'''
# Operadores: > < >= <= != ==
if fruta == 'Kiwi' :
	print("El valor es Kiwi")
else:
	print("No son iguales")

#Minificando codigo, poniendo todo en una linea
mensaje = 'El valor es kiwi' if fruta == 'kiwi' else 'No son iguales'
print (mensaje)
#Minificar codigo, solo si es un solo valor a comparar
if fruta == 'Kiwi':
	print("El valor es un kiwi")
elif fruta == 'Manzana':
	print("El valor es Manzana")
else:
	print("No son iguales")

''' Es muy necesaria la identacion, para que funcione '''
if fruta == 'Kiwi':
	pass #Si no tenemos nada que poneer, si lo dejo vacio dara error

#True = 1
#False = 0
if 1:
	print("Es verdad")
else: 
	print("No es verdad")
#[] = False
#[1,2,3] = True
if []:
	print("Es verdad")
else:
	print("No es verdad")

#Palabra reservada None para decir que no tiene valor
valor = None
if valor:
	print("Es verdad")
else:
	print("No es verdad")
valor2 = 21
#Codicional de dos condiciones
#And = Deben cumplirse todos
if valor and valor_dos > 20:
	print("Es verdad")
else:
	print("No es verdad")
#Or = Por lo menos debe cumplirse uno
if valor or valor2 > 20:
	print("Es verdad")
else:
	print("No es verdad")

