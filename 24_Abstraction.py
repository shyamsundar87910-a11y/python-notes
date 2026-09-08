# ===================== OOP - ABSTRACTION =====================


# .........................Basic Abstraction.........................#

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()


# .........................Abstract Class.........................#

from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def show(self):
        pass


class BCAStudent(Student):

    def show(self):
        print("BCA Student")


student1 = BCAStudent()

student1.show()


# .........................Abstract Method.........................#

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):

    def sound(self):
        print("Cat meows")


cat1 = Cat()

cat1.sound()


# .........................Abstraction with Multiple Methods.........................#

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


car1 = Car()

car1.start()
car1.stop()


# .........................Abstraction with Attributes.........................#

from abc import ABC, abstractmethod


class Student(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_course(self):
        pass


class BCAStudent(Student):

    def show_course(self):
        print(self.name)
        print("Course: BCA")


student1 = BCAStudent("Shyam")

student1.show_course()


# .........................Abstraction with Calculation.........................#

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(10, 5)

print(rectangle1.area())


# .........................Abstraction with Different Classes.........................#

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog1 = Dog()
cat1 = Cat()

dog1.sound()
cat1.sound()


# .........................Abstraction with Inheritance.........................#

from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        print("Developer writes code")


class Designer(Employee):

    def work(self):
        print("Designer creates designs")


developer1 = Developer()
designer1 = Designer()

developer1.work()
designer1.work()


# .........................Cannot Create Object of Abstract Class.........................#

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# animal1 = Animal()

# This will give an error because
# Animal is an abstract class.
