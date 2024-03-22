### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

# Definir

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        # Variables por separado
        #self.name = name
        #self.surname = surname
        # Unión en una misma variable
        self.full_name = f"{name} {surname} ({alias})" #Propiedad pública
        self.__name = name #Propiedad privada
    
    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person("David", "Couñago")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("David", "Couñago", "DavidCG")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)

# Predefinido

class Person:
    def __init__(self):
        self.name = "David"
        self.surname = "Couñago"

my_person = Person()
print(f"{my_person.name} {my_person.surname}")
