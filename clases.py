#Las clases deben comenzar en mayuscula
#Si son mas de dos plabras la conversion debe ser asi "LapizAmarillo"
#Declarar atributos privado "__atributo"
'''Clase 1'''
class Lapiz:
	#Metodos
	def __init__(self,color = 'Amarillo',contiene_borrador = False,usa_graffito = True):
		#Atributos
		self.color = color
		self.contiene_borrador = contiene_borrador
		self.usa_graffito = usa_graffito

	def dibujar(self):
		print("El lapiz esta dibujando")
	def borrar(self):
		if self.es_valido_para_borrar():
			print("El lapiz esta borrando")
		else:
			print("No es posible borrar")
		
	def es_valido_para_borrar(self):
		return self.contiene_borrador 
'''Clase 2'''
class Usuario:
	def __init__(self,username,password,email):
		self.username = username
		self.__password = self.__generar_password(password)
		self.email = email
	def __generar_password(self,password):
		return password.upper()
	def get_password(self):
		return self.__password
'''Clase 3'''
class Circulo:
	__pi = 3.1416
	def __init__(self,radio):
		self.radio = radio
	def area(self):
		return self.radio * self.__pi




#Esto es un objeto
'''lapiz_generico = Lapiz("Verde",True,True)
lapiz_generico.dibujar()
lapiz_generico.borrar()'''
#Segunda clase
'''eduardo = Usuario('eduardo','eduardo123','eduardo@codigofacilito.com')
print(eduardo.username)
print(eduardo.email)
print(eduardo.get_password())'''

circulo_uno = Circulo(4)
circulo_dos = Circulo(6)

print(circulo_uno.area())