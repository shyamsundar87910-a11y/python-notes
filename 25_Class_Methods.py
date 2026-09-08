# ===================== OOP - CLASS METHODS =====================


# .........................Basic Class Method.........................#

class Student:

    @classmethod
    def show(cls):
        print("This is a class method")


Student.show()


# .........................Class Method with Class Variable.........................#

class Student:

    name = "Shyam"

    @classmethod
    def show(cls):
        print(cls.name)


Student.show()


# .........................Class Method with Multiple Class Variables.........................#

class Student:

    name = "Shyam"
    age = 20
    course = "BCA"

    @classmethod
    def show(cls):
        print(cls.name)
        print(cls.age)
        print(cls.course)


Student.show()


# .........................Class Method with Parameter.........................#

class Student:

    @classmethod
    def show(cls, name):
        print("Student Name:", name)


Student.show("Shyam")


# .........................Class Method with Class Attribute Update.........................#

class Student:

    name = "Shyam"

    @classmethod
    def change_name(cls, name):
        cls.name = name


print(Student.name)

Student.change_name("Rahul")

print(Student.name)


# .........................Class Method with Multiple Attributes.........................#

class Student:

    name = "Shyam"
    age = 20

    @classmethod
    def update_data(cls, name, age):
        cls.name = name
        cls.age = age


print(Student.name)
print(Student.age)

Student.update_data("Rahul", 21)

print(Student.name)
print(Student.age)


# .........................Calling Class Method using Object.........................#

class Student:

    name = "Shyam"

    @classmethod
    def show(cls):
        print(cls.name)


student1 = Student()

student1.show()


# .........................Class Method with Multiple Objects.........................#

class Student:

    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def show_count(cls):
        print("Total Students:", cls.count)


student1 = Student()
student2 = Student()
student3 = Student()

Student.show_count()


# .........................Class Method with Constructor.........................#

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_school(cls):
        print("School:", cls.school)


student1 = Student("Shyam")

Student.show_school()


# .........................Class Method vs Instance Method.........................#

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        print("Student:", self.name)

    @classmethod
    def show_school(cls):
        print("School:", cls.school)


student1 = Student("Shyam")

student1.show_student()
Student.show_school()


# .........................Class Method with Calculation.........................#

class Calculator:

    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b


print(Calculator.add(10, 20))
print(Calculator.multiply(10, 20))


# .........................Class Method with if else.........................#

class Student:

    passing_marks = 40

    @classmethod
    def check_result(cls, marks):

        if marks >= cls.passing_marks:
            print("Pass")
        else:
            print("Fail")


Student.check_result(75)
Student.check_result(30)
