course = 'Curso'
my_string = "Codigo Facilito"
''' Metodos de formato '''
result = '{} de {}'.format(course,my_string) #Concatenar con el metodo format
result = '{a} de {b}'.format(a = course, b = my_string) #Ahora con alias
result = result.lower() #Este metodo coloca todo en minusculas
#result = result.upper() #Este metodo coloca todo en mayusculas
#result = result.title() #Pone el string como un titulo

print(result)

''' Metodo de Busqueda '''
pos = result.find('Codigo') #Y con este sabemos la posicion de la misma
count = result.count('c') #Con este metodo podemos saber cuantas veces se repite la letra c
print(count)

''' Metodo de Sustitucion '''
new_string = result.replace('c','x') #para reemplazar palabra o letra
new_string = result.split(' ') #Convierte la cadena en un array, cada vez que encuentre un espacio
print(new_string)
