#FUNCIONES

def factorial_numero(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -=1
	return factorial

print factorial_numero(4)
print factorial_numero(5)
print factorial_numero(6)

