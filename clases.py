#Las clases deben comenzar en mayuscula
#Si son mas de dos plabras la conversion debe ser asi "LapizAmarillo"
class Lapiz:
	#Atributos
	color = 'Amarillo'
	contiene_borrador = False
	usa_graffito = True
	#Metodos
	def dibujar(self):
		print("El lapiz esta dibujando")
	def borrar(self):
		if self.es_valido_para_borrar():
			print("El lapiz esta borrando")
		else:
			print("No es posible borrar")
		
	def es_valido_para_borrar(self):
		return self.contiene_borrador 


#Esto es un objeto
lapiz_generico = Lapiz()
lapiz_generico.dibujar()
lapiz_generico.borrar()
print (lapiz_generico.color)