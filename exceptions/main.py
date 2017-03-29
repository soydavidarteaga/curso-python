class TinyIntError(Exception):
	pass

def tiny_int(val):
	return val >= 0 and val <= 255

try:
	numero = 400
	if tiny_int(numero):
		print("El numero es correcto")
	else:
		raise TinyIntError("Este es un mensaje para los numeros que no son tinyInt")
except TinyIntError as error:
	print("No es posible completar la operacion: {}".format(error))
