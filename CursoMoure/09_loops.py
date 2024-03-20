### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional, podríamos simplemente poner el print fuera del bucle
    print("Mi condición ya es igual o mayor que 10")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15, detenemos")
        break
    print(my_condition)

    # For

my_list = [21, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (21, 1.75, "David", "Couñago", "David")
for element in my_tuple:
    print(element)

my_set = {"David", "Couñago", 21}
for element in my_set:
    print(element)

my_dict = {"Nombre":"David", "Apellido":"Couñago", "Edad":21, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        #break rompe el bucle
        continue # Salta directamente al siguiente loop sin realizar lo que quede por debajo en el for
    print("Se ejecuta")
else:
    print("El bucle for a termiando")