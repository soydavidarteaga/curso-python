
'''
lista = []
for valor in range(0,101):
	lista.append(valor)
'''

lista = [ valor for valor in range(0,101) ] #Comprenhension.
#1. Valor a agregar a una lista
#2. Un ciclo, for
lista = [ valor for valor in range(0,101) if valor % 2 == 0 ] #Con condicion
print(lista)

tupla = tuple(valor for valor in range(0,101) if valor % 2 != 0)
print(tupla)

diccionario = { indice:valor for indice, valor in enumerate(lista) } #Ahora con diccionario

print(diccionario)