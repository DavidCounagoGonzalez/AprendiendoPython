### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String con \\n escapado"
print(my_scape_string)

#Formato

name, surname, age = 'David', 'Couñago', 21

print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
#Con % nos aseguramos a la vez de que el tipo de dato sea el que queremos
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age))
#Forma clásica
print("Mi nombre es " + name + " " + surname + " y tengo " + str(age) + " años ")
#Forma sencilla 
print(f"Mi nombre es {name} {surname} y tengo {age} años")

#Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

#División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith('py'))