### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (21, 1.75, "David", "Couñago", "David")
my_other_tuple = (21, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("David"))
print(my_tuple.index("Couñago"))
print(my_tuple.index("David"))

#my_tuple[1] = 1.80 El objeto tupla no permite asignar elementos

#Concatnación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

#Subtuplas

print(my_sum_tuple[3:6]) 

#Tupla mutable mediante conversión a lista

my_tuple = list(my_tuple)

print(type(my_tuple))

my_tuple[4] = "DavidCG"
my_tuple.insert(1, "Rosa")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2]  TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined