### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [21, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [21, 1.75, "David", "Couñago"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list[len(my_other_list) -1])
print(my_list.count(30))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, heigth, name, surname = my_other_list
print(name)

name, heigth, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

my_other_list.append("DavidCG") #Inserta el valor al final
print(my_other_list)

my_other_list.insert(1, "Violeta") #Inserta el valor en la posición indicada moviendo el resto
print(my_other_list)

my_other_list[1] = "Rosa" #Cambia el valor en esa posición
print(my_other_list)

my_other_list.remove("Rosa") #Borra el elemento que sea igual a lo indicado
print(my_other_list)

my_list.remove(30) #Como hay dos 30 elimina solo el primero que encuentra en la lista
print(my_list)

print(my_list.pop()) #Devuelve y elimina el último elemento
print(my_list)

my_pop_element = my_list.pop(2) #Se le puede pasar un índice
print(my_pop_element)
print(my_list)

del my_list[2] #Elimina el elemento de esa posición
print(my_list)

my_new_list = my_list.copy() #Guarda una copia en otra variable de la lista

my_list.clear() #Vacía la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #Invierto el orden de los elementos
print(my_new_list)

my_new_list.sort() #Ordena por orden alfabético o númerico los elementos de la lista
print(my_new_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))