# ===================== OOP - CLASSES & OBJECTS =====================

# .........................Create Class.........................#

class Student:
    pass


# .........................Create Object.........................#

class Student:
    pass

student1 = Student()

print(student1)


# .........................Class Attribute.........................#

class Student:
    name = "Shyam"
    age = 20

student1 = Student()

print(student1.name)
print(student1.age)


# .........................Multiple Objects.........................#

class Student:
    name = "Shyam"

student1 = Student()
student2 = Student()

print(student1.name)
print(student2.name)


# .........................Object Attributes.........................#

class Student:
    pass

student1 = Student()

student1.name = "Shyam"
student1.age = 20

print(student1.name)
print(student1.age)


# .........................Class Method.........................#

class Student:

    def show(self):
        print("Hello Shyam")

student1 = Student()

student1.show()


# .........................Method with Attributes.........................#

class Student:

    def show(self):
        print(self.name)
        print(self.age)

student1 = Student()

student1.name = "Shyam"
student1.age = 20

student1.show()


# .........................Multiple Methods.........................#

class Calculator:

    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

calculator = Calculator()

calculator.add(10, 20)
calculator.subtract(20, 10)


# .........................Object with Different Values.........................#

class Student:

    def show(self):
        print(self.name)
        print(self.age)

student1 = Student()
student1.name = "Shyam"
student1.age = 20

student2 = Student()
student2.name = "Rahul"
student2.age = 21

student1.show()
student2.show()


# .........................Class with Calculation.........................#

class Rectangle:

    def area(self, length, width):
        return length * width

rectangle = Rectangle()

print(rectangle.area(10, 5))


# .........................Class with if else.........................#

class Student:

    def check_result(self, marks):

        if marks >= 40:
            print("Pass")
        else:
            print("Fail")

student1 = Student()

student1.check_result(75)


# .........................Class with List.........................#

class Student:

    def show_marks(self, marks):

        for mark in marks:
            print(mark)

student1 = Student()

student1.show_marks([80, 85, 90])


# .........................Class with Dictionary.........................#

class Student:

    def show_data(self, data):

        for key, value in data.items():
            print(key, value)

student1 = Student()

student1.show_data({
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
})
