#FUNCIONES

def factorial_numero(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -=1
	return factorial

'''
print factorial_numero(4)
print factorial_numero(5)
print factorial_numero(6) '''

#Fin Clase 1

#Clase 2
def suma(v1,v2,v3):
	return v1 + v2 + v3
def division(v1,v2):
	return v1 / v2
def multiplicacion(v1,v2 = 10): #Valor por defecto
	return v1 * v2
def multiples_valores():
	return "String",1,True,25.6

print suma(10,20,30)
print division(v1 = 100, v2 = 10) #Ideal para cuando conozca el nombre de los argumentos
print multiplicacion(6,15)

string, entero, bol, floa = multiples_valores()

print string
print entero
print bol
print floa

mi_variable = multiplicacion #Poniendole funcion a una variable
print mi_variable(6,8)

def mostrar_resultado( funcion ):
	print(funcion(6,8))
mostrar_resultado(mi_variable)

