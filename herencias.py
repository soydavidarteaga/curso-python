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
	name = '' #Todas las mascotas necesita un nombre
	def get_name(self):
		print(self.name)
class Gato(Felino,Mascota):
	pass
class Jaguar(Felino):
	pass

gato = Gato()
jaguar = Jaguar()

gato.cazar()
gato.name = "Juancho"
gato.get_name()
print(gato.terrestre)
