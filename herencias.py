class Animal:
	@property
	def terrestre(self):
		return True
class Felino(Animal): #Clase Padre
	@property
	def garras_retractiles(self):
		return True
	def cazar(self):
		print("El felino esta cazando")
class Mascota:
	def __init__(self,name):
		self.name = name #Todas las mascotas necesita un nombre
	def get_name(self):
		print(self.name)
class Gato(Felino,Mascota):
	def __init__(self,name):
		Mascota.__init__(self,name)
		self.name_gato = name
	def get_name(self):#Sobre escritura de metodos
		Mascota.get_name(self)
		print("El nombre de el Gato es: {}".format(self.name))
class Jaguar(Felino):
	pass

gato = Gato('Patricio')
jaguar = Jaguar()

gato.cazar()
gato.get_name()
print(gato.terrestre)
