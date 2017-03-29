class TinyIntError(Exception):
	def __init__(self):
		self.message = "El numero no cuenta con las caracteristicas de un numero tinyInt"
	def __str__(self):
		return self.message