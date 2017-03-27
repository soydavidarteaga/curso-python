#!/usr/bin/env python
# -*- coding: utf-8 -*-
#FUNCIONES

def factorial_numero(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -=1
	return factorial


print factorial_numero(4)
print factorial_numero(5)
print factorial_numero(6) 


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


#Clase 3

frase = 'anita lava la tina' #Variables Globales
def palindromo():
	valor = frase.replace(' ','') #Variables Locales
	return valor == valor[::-1]

resultado = palindromo()
print(frase)
print resultado


variable_global = 'Esto es un variable Global'

def valor_global():
	global variable_global
	variable_global = 'Cambio de valor'

print(variable_global)
valor_global()
print(variable_global)

def crear_global():
	global nueva_variable
	nueva_variable = 'Esto es una variable global'

crear_global()
print(nueva_variable)


#Clase 4
def suma(*argumentos):
	resultado = 0
	for argumento in argumentos:
		resultado = resultado + argumento
	return resultado
print suma(5,2,3)

def suma(**kwargs):
	valor = kwargs.get('valor','No contiene el valor')
	return valor
print suma(y = 9,z=3,d=4)

#Clase 5: Lambdas

mi_funcion = lambda v1,v2:  v1 + v2
print mi_funcion(50,10)
formato = lambda sentencia: '¿{}?'.format(sentencia)
no_valor = lambda:10
print(formato('Puedes hacer esto una pregunta'))
print no_valor()

#Clase 6: Funciones Anidadas

def crear_funcion(num_uno,num_dos):
	#Closure
	def validacion():
		print "Se ejecuta una funcion"
		return num_uno > 0 and num_dos > 0
	return validacion
def aplicar_funcion(func):
	print func()

nueva_funcion = crear_funcion(10,-5)
aplicar_funcion(nueva_funcion)

#Clase 7: Decoradores
#Un decorador nos va a ayudar a darle mayor funcionalidad a una funcion, es una funcion que recibe como parametro un funcion para poder crear c
#A recibe como parametro B para poder crear C
def decorator(is_valid):
	def decorador(func): #A,B 
		def before_action():
			print("Vamos a ejecutar la funcion")
		def after_action():
			print("Se ejecuto la funcion")
		def nueva_funcion(*args,**kwargs):
			if is_valid:
				before_action()
			return func(*args,**kwargs)
			after_action()
		return nueva_funcion #C
	return decorador

@decorator(is_valid = True) 
def saluda():
	print("Hola Mundo")
saluda()
@decorator(is_valid = False)
def suma(n1,n2):
	return n1 + n2
print suma(180,17)

#Clase 8: Generadores
'''Nos sirven para crear objetos sin necesidad de almacenarlo en la memoria ram, por lo general se trabaja con loops, siempre que creemos un generador se utiliza la palabra reservada yield'''


def generador(*args):
	for valor in args:
		yield valor * 10

for valor in generador(1,2,3,4,5,6,7,8,9,10):
	print(valor)

#Clase 9: DocString
def generadorDOc(*args):
	"""Recibe N cantidad de numero y regresa el numero ademas de regresa True o False si el numero es mayor a 5 
	"""
	for valor in args:
		yield valor * 10

name = generador.__name__
documentacion = generadorDOc.__doc__

print(name, " : ")
print(documentacion)

'''Con interprete de python. Pasos 1 poner en consola: python3 , paso 2 poner en consola: from nombre_archivo import nombre_de_la_funcion Paso 3 poner en consola: help( nombre_de_la_funcion ) '''
