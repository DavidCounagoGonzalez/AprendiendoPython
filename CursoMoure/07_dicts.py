### Dictionaries ###

my_dict = dict()
my_other_dict = {} #Aunque así se definan los sets, al estar vacíos su tipo es dict

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"David", "Apellido":"Couñago", "Edad":21, 1:"Python"}

my_dict={
    "Nombre":"David",
    "Apellido":"Couñago",
    "Edad":21,
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.75
}

print(my_other_dict)
print(my_dict)

print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict['Calle'] = "Calle DavidCG"
print(my_dict)

del my_dict['Calle']
print(my_dict)

print("Couñago" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nomrbe", 1, "Piso"]

#my_new_dict = my_other_dict.fromkeys(("Nomrbe", 1, "Piso"))
my_new_dict = dict.fromkeys(my_list) #fromkeys crea un dict añadiendole las claves según los valores pasados
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict) #Crea uan copia de estructura del dict por parámetro 
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "DavidCG")  #El segundo parámetro no permite asignar key->Value, simplemente lo repite en todas las keys
print(my_new_dict)

print(list(my_new_dict)) # Al transformarlo en una lista solo se guardan las claves
print(tuple(my_new_dict))
print(set(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values)) # class dict_values

print(list(my_new_dict.values())) # Necesitamos .values() para recoger estos mismos en la lista

print(dict.fromkeys(list(my_values))) 
# Lo que hace es crear un dict con key = a los values de la lista que en este caso solo sale uan vez por repetición

# Fumada/Apuntarse a uno mismo
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))

