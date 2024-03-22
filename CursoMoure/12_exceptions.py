### Exceptions Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    #Se ejecuta si hay una excepción
    print("Se ha producido un error")

# try except else
    
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: #Opcional
    #Se ejecuta si no hay una excepción
    print("La ejecución continúa correctamente")
finally: #Opcional
    #Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError:
    #Se ejecuta si hay una excepción
    print("Se ha producido un ValueError")
except TypeError:
    #Se ejecuta si hay una excepción
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:
    #Se ejecuta si hay una excepción
    print(error)
except Exception as exception:
    print(exception)