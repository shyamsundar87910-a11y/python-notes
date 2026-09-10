# ===================== 31_LAMBDA_FUNCTIONS.py =====================


# .........................Basic Lambda Function.........................#

square = lambda x: x * x

print(square(5))


# .........................Lambda with Two Parameters.........................#

add = lambda a, b: a + b

print(add(10, 20))


# .........................Lambda with Multiple Parameters.........................#

multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))


# .........................Lambda with if else.........................#

check_number = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_number(10))
print(check_number(7))


# .........................Lambda with String.........................#

name_length = lambda name: len(name)

print(name_length("Python"))


# .........................Lambda with Uppercase.........................#

upper_name = lambda name: name.upper()

print(upper_name("rahul"))


# .........................Lambda with List.........................#

numbers = [1, 2, 3, 4, 5]

square = lambda x: x * x

for number in numbers:
    print(square(number))


# .........................Lambda with List Sorting.........................#

students = [
    ("Aman", 80),
    ("Rahul", 60),
    ("Riya", 90)
]

students.sort(key=lambda student: student[1])

print(students)


# .........................Lambda with Dictionary.........................#

student = {
    "name": "Aman",
    "marks": 85
}

get_marks = lambda data: data["marks"]

print(get_marks(student))


# .........................Lambda with Calculation.........................#

calculate = lambda a, b: (a + b) * 2

print(calculate(10, 20))


# .........................Lambda with Multiple Operations.........................#

numbers = [10, 20, 30, 40, 50]

double = lambda x: x * 2

for number in numbers:
    print(double(number))
