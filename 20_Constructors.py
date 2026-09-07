# ===================== CONSTRUCTORS =====================


# .........................Basic Constructor.........................#

class Student:

    def __init__(self):
        print("Student object created")


student1 = Student()
student2 = Student()


# .........................Constructor with Parameters.........................#

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Aman", 20)

print(student1.name)
print(student1.age)


# .........................Multiple Attributes.........................#

class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


employee1 = Employee("Rahul", 30000, "IT")

print(employee1.name)
print(employee1.salary)
print(employee1.department)


# .........................Multiple Objects.........................#

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Aman", 85)
student2 = Student("Riya", 92)

print(student1.name, student1.marks)
print(student2.name, student2.marks)


# .........................Default Values.........................#

class Student:

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


student1 = Student("Aman")
student2 = Student("Riya", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)


# .........................Constructor + Method.........................#

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Aman", 85)

student1.display()


# .........................Constructor with Calculation.........................#

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r1 = Rectangle(10, 5)

print("Area:", r1.area())


# .........................Constructor with If-Else.........................#

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):

        if self.marks >= 40:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")


student1 = Student("Aman", 75)
student2 = Student("Rahul", 30)

student1.result()
student2.result()


# .........................Constructor with List.........................#

class Student:

    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects


student1 = Student(
    "Aman",
    ["Math", "Science", "English"]
)

print(student1.name)
print(student1.subjects)


# .........................Constructor with Dictionary.........................#

class Employee:

    def __init__(self, details):
        self.details = details


employee1 = Employee({
    "name": "Aman",
    "salary": 30000,
    "department": "IT"
})

print(employee1.details)


# .........................Constructor + Average.........................#

class Student:

    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def average(self):
        avg = (self.math + self.science + self.english) / 3
        print("Name:", self.name)
        print("Average:", avg)


student1 = Student("Aman", 80, 85, 90)

student1.average()


# .........................Constructor + Salary Check.........................#

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def check_salary(self):

        if self.salary >= 30000:
            print(self.name, "has a good salary")
        else:
            print(self.name, "salary is below 30000")


employee1 = Employee("Aman", 35000)
employee2 = Employee("Rahul", 25000)

employee1.check_salary()
employee2.check_salary()
