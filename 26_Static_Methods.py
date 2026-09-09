# ===================== OOP - STATIC METHODS =====================


# .........................Basic Static Method.........................#

class Student:

    @staticmethod
    def show():
        print("This is a static method")


Student.show()


# .........................Static Method with Parameters.........................#

class Calculator:

    @staticmethod
    def add(a, b):
        print(a + b)


Calculator.add(10, 20)


# .........................Static Method with Multiple Parameters.........................#

class Calculator:

    @staticmethod
    def add(a, b):
        print("Addition:", a + b)

    @staticmethod
    def subtract(a, b):
        print("Subtraction:", a - b)

    @staticmethod
    def multiply(a, b):
        print("Multiplication:", a * b)


Calculator.add(10, 20)
Calculator.subtract(20, 10)
Calculator.multiply(10, 20)


# .........................Static Method with Return.........................#

class Calculator:

    @staticmethod
    def square(number):
        return number * number


result = Calculator.square(5)

print(result)


# .........................Static Method with if else.........................#

class Student:

    @staticmethod
    def check_result(marks):

        if marks >= 40:
            print("Pass")
        else:
            print("Fail")


Student.check_result(75)
Student.check_result(30)


# .........................Static Method with String.........................#

class Student:

    @staticmethod
    def welcome(name):
        print("Welcome", name)


Student.welcome("Shyam")


# .........................Static Method with List.........................#

class Student:

    @staticmethod
    def show_marks(marks):

        for mark in marks:
            print(mark)


Student.show_marks([80, 85, 90])


# .........................Static Method with Dictionary.........................#

class Student:

    @staticmethod
    def show_data(data):

        for key, value in data.items():
            print(key, value)


Student.show_data({
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
})


# .........................Calling Static Method using Object.........................#

class Student:

    @staticmethod
    def show():
        print("Hello Shyam")


student1 = Student()

student1.show()


# .........................Static Method with Class Method.........................#

class Student:

    school = "ABC School"

    @staticmethod
    def show_message():
        print("Welcome to Student Class")

    @classmethod
    def show_school(cls):
        print("School:", cls.school)


Student.show_message()
Student.show_school()


# .........................Static Method with Instance Method.........................#

class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

    @staticmethod
    def show_course():
        print("Course: BCA")


student1 = Student("Shyam")

student1.show_name()
Student.show_course()


# .........................Static Method for Validation.........................#

class Student:

    @staticmethod
    def check_age(age):

        if age >= 18:
            return True
        else:
            return False


print(Student.check_age(20))
print(Student.check_age(15))


# .........................Static Method with Calculation.........................#

class Math:

    @staticmethod
    def square(number):
        return number * number

    @staticmethod
    def cube(number):
        return number * number * number


print(Math.square(5))
print(Math.cube(3))
