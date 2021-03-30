# SOLID PRINCIPLES IN PYTHON
# --------------------------

# 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ----------------------------------------
# --- DEFINITION:
# A class should have only one job to avoid becoming coupled.

# --- DON'T DO
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        pass

    def save(self):
        pass

# --- SRP
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        pass

class AnimalDB:
    def save(self, animal: Animal):
        pass

ape = Animal('ape')
AnimalDB().save(ape)


# 2. OPEN-CLOSED PRINCIPLE (OCP)
# ------------------------------
# --- DEFINITION:
# Software entities(Classes, modules, functions) should be open for extension, not modification.

# --- DON'T DO
animals = [Animal('lion'), Animal('mouse')]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')

animal_sound(animals)


# --- OCP
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'roar'

class Mouse(Animal):
    def make_sound(self):
        return 'squeak'

class Snake(Animal):
    def make_sound(self):
        return 'hiss'

class Ant(Animal):
    def make_sound(self):
        return 'chirp'

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Lion('l'), Mouse('m'), Snake('s')]
animal_sound(animals)


# 3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
# --------------------------------------
# --- DEFINITION:
# A sub-class must be substitutable for its super-class.

# --- DON'T DO
def lion_leg_count(animal: str):
    return 4

def ant_leg_count(animal: str):
    return 6

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Ant):
            print(ant_leg_count(animal))

animals = [Lion('l'), Ant('a')]
animal_leg_count(animals)


# --- LSP
l = Lion('l')
m = Mouse('m')
a = Animal('a')

def animal_sound(animal: Animal):
    print(animal.make_sound())

animal_sound(m)
animal_sound(a)


# 4. INTERFACE SEGREGATION PRINCIPLE (ISP)
# ----------------------------------------
# --- DEFINITION:
# Clients should not be forced to depend on methods that they do not use.

# --- DON'T DO:
class Shape:
    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

class Circle(Shape):
    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

class Rectangle(Shape):
    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

Circle().draw_rectangle()

# --- ISP
class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        pass

Circle().draw()


# 5. DEPENDENCY INVERSION PRINCIPLE (DIP)
# ---------------------------------------
# --- DEFINITION:
# Any higher classes should always depend upon the abstraction of the class rather than the detail.

# --- DON'T DO:
class Manager(object):
    def __init__(self):
        self.developers = []
        self.designers = []

    def add_developer(self, dev):
        self.developers.append(dev)

    def add_designers(self, des):
        self.designers.append(des)


class Developer(object):
    def __init__(self):
        pass

class Designer(object):
    def __init__(self):
        pass

m = Manager()
m.add_developer(Developer())
m.add_designers(Designer())


# --- DIP
class Employee(object):
    pass

class Manager():
    def __init__(self):
        self.employees = []

    def add_employee(self, a):
        self.employees.append(a)


class Developer(Employee):
    def __init__(self):
        print("developer added")


class Designer(Employee):
    def __init__(self):
        print("designer added")

m = Manager()
m.add_employee(Developer())
m.add_employee(Designer())






