# .........................Basic Generator.........................#

def numbers():
    yield 10
    yield 20
    yield 30


result = numbers()

print(next(result))
print(next(result))
print(next(result))


# .........................Generator with Loop.........................#

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for number in numbers():
    print(number)


# .........................Generator with Range.........................#

def numbers():
    for number in range(1, 6):
        yield number


for number in numbers():
    print(number)


# .........................Generator with Even Numbers.........................#

def even_numbers():
    for number in range(1, 11):
        if number % 2 == 0:
            yield number


for number in even_numbers():
    print(number)


# .........................Generator with Odd Numbers.........................#

def odd_numbers():
    for number in range(1, 11):
        if number % 2 != 0:
            yield number


for number in odd_numbers():
    print(number)


# .........................Generator with String.........................#

def characters(word):
    for character in word:
        yield character


for character in characters("Python"):
    print(character)


# .........................Generator with List.........................#

def students():
    student_list = ["Aman", "Riya", "Rahul", "Sneha"]

    for student in student_list:
        yield student


for student in students():
    print(student)


# .........................Generator with Calculation.........................#

def squares():
    for number in range(1, 6):
        yield number ** 2


for square in squares():
    print(square)


# .........................Generator with Parameters.........................#

def numbers(start, end):
    for number in range(start, end + 1):
        yield number


for number in numbers(1, 5):
    print(number)


# .........................Generator with Multiple Values.........................#

def student_data():
    yield "Aman"
    yield 20
    yield "BCA"


student = student_data()

print(next(student))
print(next(student))
print(next(student))


# .........................Generator with Fibonacci Numbers.........................#

def fibonacci(limit):

    first = 0
    second = 1

    for i in range(limit):
        yield first

        first, second = second, first + second


for number in fibonacci(10):
    print(number)


# .........................Generator with if else.........................#

def check_numbers():

    for number in range(1, 6):

        if number % 2 == 0:
            yield f"{number} is Even"
        else:
            yield f"{number} is Odd"


for result in check_numbers():
    print(result)
