### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"David", "Couñago", 21}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("DavidCG")

print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add("DavidCG") #Un set no admite elementos repetidos

print(my_other_set)

print("Couñago" in my_other_set)
print("Couñagu" in my_other_set)

my_other_set.remove("Couñago")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
# print(my_other_set) Elimina la variable por completo

my_set = {"David", "Couñago", 21}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) 
#Solo se añaden los elementos del set definido porque los otros solo contienen elementos repetidos

#Difference devuelve los elementos que no coincidan con los existentes en el parámetro pasado
print(my_new_set.difference(my_set)) 
#En este caso solo salen los de my_other_set porque el union de JS y C# al hacerlo en el print no se guarda

print(my_new_set.intersection(my_set)) #Devuelve los valores que coincidan entre los sets

# Devuelve True en caso de que los elementos del primer set se encuentren en el pasado como parámetro
print(my_new_set.issubset(my_set)) # False
print(my_set.issubset(my_new_set)) # True

# Al contrario que el anterior comprueba que los elementos del parámetro estén en el set 
print(my_new_set.issuperset(my_set)) # True
print(my_set.issuperset(my_new_set)) # False