### Modules ###

import my_module

my_module.sumValue(5, 3, 7)
my_module.printValue("Hola Python")

from my_module import sumValue, printValue

my_module.sumValue(5, 3, 7)
my_module.printValue("Hola Python")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

# print(pi) # Pasa a funcionar solo mediante el alias que asginamos
print(PI_VALUE)