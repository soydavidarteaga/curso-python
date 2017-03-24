''' Arreglos '''
my_list = ['strings',15,15.6, True]
my_list.append(6) #Para agregar valores a el arreglo
my_list.insert(1,"Insert") #Otra forma de agregar valores, pero aqui lo agregamos por el indice
my_list.remove(15) #Es para remover valores.
my_list.pop() #Elimina el ultimo valor
print(my_list)

my_numbers = [1,6,5,7,2,66,4]
my_numbers.sort() #Para ordenar la lista de numeros de menor a mayor
print(my_numbers) 
my_numbers.sort(reverse = True) #Para ordenar la lista de numero de mayor a menor
print(my_numbers)

#Unir listas

my_list_two = [22,23]
my_list.extend(my_list_two) #Para unir arreglos
print(my_list)
my_list.append(my_list_two) #Para unir lista de forma literal
print(my_list)