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
class Gato(Felino):
	pass
class Jaguar(Felino):
	pass

gato = Gato()
jaguar = Jaguar()

gato.cazar()
print(gato.terrestre)
