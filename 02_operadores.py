### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(10 // 3)
print(2 ** 3)

#Operando con strings
print("Hola " + "Python " +  "¿Qué tal?")
print("Hola "+ str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))
# Para decimales que en operación dan un entero hay que parsearlo igualmente
print("Hola " * int(2.5 ** 2))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "AAAA") # Ordenación alfabética respecto a ASCII
print(len("aaaa") >= len("abaa")) #Por número de caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" < "Python" and 4 == 4))
print(not(3 > 4))
#print(3 > 4 not "Hola" > "Python")