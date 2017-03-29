#Paquete para validad errores en enteros TinyInt
##USO
***
Debes primeramente invocarlo asi `from tinyintError import tiny_int`
***
Para usarlo se hace asi: sabendo que debes indicarle un valor y un callback para los errores. `print(tiny_int(50 , call_back_function))`
***
Donde callback es una funcion que debes definir de la siguiente manera:
***
`def call_back_function():
	print("Esto se ejecuta cuando hay un error")`