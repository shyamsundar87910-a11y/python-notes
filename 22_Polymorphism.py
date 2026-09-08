# ===================== OOP - POLYMORPHISM =====================


# .........................Same Method - Different Classes.........................#

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# .........................Polymorphism with Different Objects.........................#

class Car:

    def start(self):
        print("Car starts with a key")


class Bike:

    def start(self):
        print("Bike starts with a button")


car = Car()
bike = Bike()

car.start()
bike.start()


# .........................Polymorphism with Function.........................#

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# .........................Polymorphism with Inheritance.........................#

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# .........................Method Overriding.........................#

class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        print("Child method")


parent = Parent()
child = Child()

parent.show()
child.show()


# .........................Polymorphism with Loop.........................#

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


class Cow:

    def sound(self):
        print("Cow moos")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()


# .........................Polymorphism with Calculator.........................#

class Addition:

    def calculate(self, a, b):
        print("Addition:", a + b)


class Multiplication:

    def calculate(self, a, b):
        print("Multiplication:", a * b)


addition = Addition()
multiplication = Multiplication()

addition.calculate(10, 20)
multiplication.calculate(10, 20)
