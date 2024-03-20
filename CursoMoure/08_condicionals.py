### Condicionals ###

my_condition = True

if my_condition: # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

elif my_condition > 10 and my_condition < 20: # El bloque de código de if y else se indica mediante la tabulación
    print("Es mayor que 10 y menor que 20")

elif my_condition == 25:
    print("Es igual a 25")

else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continua")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooooo":
    print("Estas cadenas de texto coinciden")