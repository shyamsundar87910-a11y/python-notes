# ===================== OOP - INHERITANCE =====================


# .........................Basic Inheritance.........................#

class Parent:

    def show(self):
        print("This is Parent class")


class Child(Parent):
    pass


child1 = Child()

child1.show()


# .........................Inheritance with Child Method.........................#

class Parent:

    def show_parent(self):
        print("This is Parent class")


class Child(Parent):

    def show_child(self):
        print("This is Child class")


child1 = Child()

child1.show_parent()
child1.show_child()


# .........................Inheritance with Attributes.........................#

class Student:

    name = "Shyam"
    course = "BCA"


class StudentDetails(Student):
    pass


student1 = StudentDetails()

print(student1.name)
print(student1.course)


# .........................Inheritance with self.........................#

class Student:

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


class BCAStudent(Student):

    def set_data(self, name, age):
        self.name = name
        self.age = age


student1 = BCAStudent()

student1.set_data("Shyam", 20)
student1.show()


# .........................Method Overriding.........................#

class Student:

    def show(self):
        print("This is Student class")


class BCAStudent(Student):

    def show(self):
        print("This is BCA Student class")


student1 = BCAStudent()

student1.show()


# .........................Inheritance with Calculation.........................#

class Calculator:

    def add(self, a, b):
        print("Addition:", a + b)


class AdvancedCalculator(Calculator):

    def multiply(self, a, b):
        print("Multiplication:", a * b)


calculator = AdvancedCalculator()

calculator.add(10, 20)
calculator.multiply(10, 20)


# .........................Multilevel Inheritance.........................#

class Grandparent:

    def show_grandparent(self):
        print("Grandparent class")


class Parent(Grandparent):

    def show_parent(self):
        print("Parent class")


class Child(Parent):

    def show_child(self):
        print("Child class")


child1 = Child()

child1.show_grandparent()
child1.show_parent()
child1.show_child()


# .........................Multiple Inheritance.........................#

class Father:

    def father(self):
        print("Father class")


class Mother:

    def mother(self):
        print("Mother class")


class Child(Father, Mother):
    pass


child1 = Child()

child1.father()
child1.mother()


# .........................Hierarchical Inheritance.........................#

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


dog1 = Dog()
cat1 = Cat()

dog1.eat()
dog1.bark()

cat1.eat()
cat1.meow()
