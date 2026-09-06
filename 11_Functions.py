# ===================== FUNCTIONS =====================

# .........................Basic Function.........................#

def greet():
    print("Hello Shyam")

greet()


# .........................Function with Parameter.........................#

def greet(name):
    print("Hello", name)

greet("Shyam")


# .........................Multiple Parameters.........................#

def add(a, b):
    print(a + b)

add(10, 20)


# .........................return.........................#

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# .........................Default Parameter.........................#

def greet(name="Shyam"):
    print("Hello", name)

greet()
greet("Rahul")


# .........................Keyword Arguments.........................#

def student(name, age):
    print(name)
    print(age)

student(age=20, name="Shyam")


# .........................*args.........................#

def add(*numbers):
    print(sum(numbers))

add(10, 20, 30)
add(10, 20, 30, 40, 50)


# .........................**kwargs.........................#

def student(**data):
    print(data)

student(name="Shyam", age=20, course="BCA")


# .........................Function with if else.........................#

def check_number(number):

    if number > 0:
        return "Positive"
    else:
        return "Negative"

print(check_number(10))


# .........................Function with Loop.........................#

def print_numbers(numbers):

    for number in numbers:
        print(number)

print_numbers([10, 20, 30, 40])


# .........................Maximum Number.........................#

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 20))


# .........................Average.........................#

def average(numbers):

    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]

print(average(numbers))
