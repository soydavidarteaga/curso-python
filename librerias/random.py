import random
print random.randint(0,10)
lista = [True, "String",23,False]
print random.choice(lista) #Imprimir valores de una lista aleatorias
print lista
random.shuffle(lista)
print lista