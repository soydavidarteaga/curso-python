''' QUe es un diccionario, es un lugar donde se pueden almacenar distintos tipos de datos '''
diccionario = { 'a' : True, 5 : 'esto es un string', (1,2) : False } #Las claves deben de ser inmutables
#Es como declarar un json en javasript
diccionario['c'] = 'Nuevo string' #Para agregar una nueva clave
diccionario['a'] = False #Asi modificamos esta clave
#Si la llave/ clave se encuentra actualiza si no crea
obtener = diccionario['a'] #Para obtener valores, solo que de no encontrarlo dara error
valor = diccionario.get('z', "No se encontraron valores") #Para obtener valor, y en caso de no encontrarlo te da esta respuesta
del diccionario[5] #Nos ayuda a eliminar
print(diccionario)
print(valor)
llaves = diccionario.keys() #Asi obtenemos solo las llaves
llaves = list(diccionario.keys()) #Asi la convertimos en lista
valores = list(diccionario.values()) #Obtenemos valores en una lista
print(llaves)
print(valores)
valores = tuple(diccionario.values()) #Obtenemos valores en una tupla
print(valores)
'''Agregar valores de diccionario a diccionario '''
diccionario_dos = {'z':23,'w':88}
diccionario['z'] = diccionario_dos['z']
diccionario['w'] = diccionario_dos['w']
print(diccionario)
diccionario.update(diccionario_dos) #Una forma mas comoda de actualizar un diccionario
print(diccionario)