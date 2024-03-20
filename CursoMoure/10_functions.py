### Function ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values(52131, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"Me llamo {name} {surname}")

print_name("David", "Couñago")

def print_name_with_default(name, surname, alias = "No me llamo"): #Indicar un valor por defecto en caso de que no se reciba
    print(f"Me llamo {name} {surname} o {alias}")

print_name_with_default("David", "Couñago")
print_name_with_default("David", "Couñago", "DavidCG")

def print_texts(*texts): # Con el asterisco podemos convertir el parametro en una tupla para que pueda recibir varios valores
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "DavidCG")