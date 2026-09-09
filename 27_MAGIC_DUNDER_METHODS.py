# ===================== OOP - MAGIC / DUNDER METHODS =====================


# .........................Basic __str__ Method.........................#

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student1 = Student("Rahul")

print(student1)


# .........................Basic __len__ Method.........................#

class Student:

    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


student1 = Student(["Python", "SQL", "Power BI"])

print(len(student1))


# .........................__add__ Method.........................#

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


number1 = Number(10)
number2 = Number(20)

print(number1 + number2)


# .........................__sub__ Method.........................#

class Number:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


number1 = Number(30)
number2 = Number(10)

print(number1 - number2)


# .........................__mul__ Method.........................#

class Number:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


number1 = Number(5)
number2 = Number(4)

print(number1 * number2)


# .........................__eq__ Method.........................#

class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


student1 = Student("Rahul")
student2 = Student("Rahul")

print(student1 == student2)


# .........................__lt__ Method.........................#

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student(60)
student2 = Student(80)

print(student1 < student2)


# .........................__gt__ Method.........................#

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


student1 = Student(90)
student2 = Student(70)

print(student1 > student2)


# .........................__repr__ Method.........................#

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"


student1 = Student("Riya", 20)

print(student1)


# .........................__getitem__ Method.........................#

class Student:

    def __init__(self, subjects):
        self.subjects = subjects

    def __getitem__(self, index):
        return self.subjects[index]


student1 = Student(["Python", "SQL", "Power BI"])

print(student1[0])
print(student1[1])


# .........................__call__ Method.........................#

class Calculator:

    def __call__(self, a, b):
        return a + b


calculator = Calculator()

print(calculator(10, 20))


# .........................__contains__ Method.........................#

class Student:

    def __init__(self, subjects):
        self.subjects = subjects

    def __contains__(self, subject):
        return subject in self.subjects


student1 = Student(["Python", "SQL", "Power BI"])

print("Python" in student1)
print("Java" in student1)
