#Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 23
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)


#Concatenar en print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Funciones del Sistema
print(len(my_string_variable ))

#Variables en una sola línea. !Cuidado con avusar de esta sintaxis¡
name, surname, alias, age = "David", "Couñago", "DavidCG", 21
print("Me llamo", name, surname, ", tengo ", age, "años y mi alias es", alias)

#Inputs (casi no se usan)

'''
first_name = input("¿Cuál es tu nombre?")
age = input("¿Cuantos años tienes?")

print(first_name)
print(age)
'''
#Cambiamos tipos
name = 35
age = "David"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = True
address = 32
address = 1.2
print(type(address))
# No se fuerza como tal simplemente en caso de el IDE tener la opción podría lanzar un warning, pero no rompe.