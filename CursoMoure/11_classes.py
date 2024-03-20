### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

# Definir

class Person:
    def __init__(self, name, surname):
        # Variables por separado
        # self.name = name
        # self.surname = surname
        self.full_name = f"{name} {surname}"

my_person = Person("David", "Couñago")
print(my_person.full_name)

# Predefinido

class Person:
    def __init__(self):
        self.name = "David"
        self.surname = "Couñago"

my_person = Person()
print(f"{my_person.name} {my_person.surname}")