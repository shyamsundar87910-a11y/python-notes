# ===================== OOP - ENCAPSULATION =====================


# .........................Public Attribute.........................#

class Student:

    name = "Shyam"
    age = 20


student1 = Student()

print(student1.name)
print(student1.age)


# .........................Public Method.........................#

class Student:

    def show(self):
        print("Student Name: Shyam")


student1 = Student()

student1.show()


# .........................Protected Attribute.........................#

class Student:

    _name = "Shyam"
    _age = 20


student1 = Student()

print(student1._name)
print(student1._age)


# .........................Protected Attribute with Child Class.........................#

class Student:

    _name = "Shyam"


class BCAStudent(Student):

    def show(self):
        print(self._name)


student1 = BCAStudent()

student1.show()


# .........................Private Attribute.........................#

class Student:

    __name = "Shyam"
    __age = 20


student1 = Student()

print(student1._Student__name)
print(student1._Student__age)


# .........................Private Attribute with Method.........................#

class Student:

    __name = "Shyam"

    def show(self):
        print(self.__name)


student1 = Student()

student1.show()


# .........................Private Method.........................#

class Student:

    def __show(self):
        print("This is a private method")

    def display(self):
        self.__show()


student1 = Student()

student1.display()


# .........................Encapsulation with Getter Method.........................#

class Student:

    def __init__(self):
        self.__name = "Shyam"

    def get_name(self):
        return self.__name


student1 = Student()

print(student1.get_name())


# .........................Encapsulation with Setter Method.........................#

class Student:

    def __init__(self):
        self.__name = "Shyam"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


student1 = Student()

print(student1.get_name())

student1.set_name("Rahul")

print(student1.get_name())


# .........................Getter and Setter with Age.........................#

class Student:

    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


student1 = Student()

print(student1.get_age())

student1.set_age(21)

print(student1.get_age())


# .........................Encapsulation with Validation.........................#

class Student:

    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")


student1 = Student()

student1.set_marks(85)

print(student1.get_marks())


# .........................Invalid Value using Setter.........................#

class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):

        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks


student1 = Student()

student1.set_marks(150)

print(student1.get_marks())
