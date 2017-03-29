'''Primera Forma de importar modulos'''
#import calculadora

#result = calculadora.suma(30,45)
#print result
'''Segunda Forma de importas modulos'''
from calculadora import suma, resta
from calculadora import multiplicacion as multiplicar #Para cambiarle el nombre a una funcionalidad
#from calculador import * Sirve para Importar todas las funcionalidades de un modulo. No se usa mucho por que se tendria que saber mucho sobre la documentacion para usarlo
print suma(30,45)