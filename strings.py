my_string = "Hola Mundo" 
my_string = "Hola Mundo 'Eduardo'"
my_string = ''' Este es un estring que contiene
saltos de linea ''' #Con tres comillas simples o comillas dobles
my_string = '''Este es un string con saltos de\n lineas ''' #Tambien se puede con slash n "\n"
course = "Python 3"
name = " Eduardo "
final_message = course + name #Se pueden unir dos strings
final_message = "Nuevo Curso de " + course + "por " + name #Primera forma de concatenar variables con strings
final_message = "Nuevo curso de %s por %s" %(course,name) #Segunda forma de concatenar variables con strings
final_message = "Nuevo Curso de {} por {}".format(course,name) #Tercera forma de concatenar variables
print(final_message)