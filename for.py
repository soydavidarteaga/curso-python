'''Ciclo For'''
lista = [1,2,3,4,5,6,7,8,9,10]
#for valor in lista:
#	pass
for valor in lista:
	print(valor)
print("Funcion range")
nuevo_rango = range(0,10)
for valor in nuevo_rango:
	print(valor)
nuevo_rango = range(20) #Va desde 0 hasta 19
for valor in nuevo_rango:
	print(valor)
nuevo_rango = range(0,20,2) #Va de dos en dos
for valor in nuevo_rango:
	print(valor)

#Primera forma de obtener indice
index = 0
for valor in lista:
	print(valor, "Tiene el indice", index)
	index += 1
#segunda forma
for index,valor in enumerate(lista):
	print(valor, "tiene el indice", index)
#Para que termine segun el tamano de una lista
for valor in range(0, len(lista)):
	print(valor)
#Recorrer string
for valor in 'Curso de codigo facilito':
	print(valor)
#Recorrer diccionario
diccionario = {'a':10,'b':20,'c':500}
for llave, valor in diccionario.items():
	print("La llave", llave,"tiene el valor de", valor)