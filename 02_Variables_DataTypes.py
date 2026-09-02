# ===================== VARIABLES & DATA TYPES =====================


# .........................Variables.........................#

name = "Shyam"
age = 20
price = 99.99

print(name)
print(age)
print(price)


# .........................Variable Naming.........................#

student_name = "Shyam"
student_age = 20

print(student_name)
print(student_age)


# .........................Multiple Variables.........................#

name, age, city = "Shyam", 20, "Jamshedpur"

print(name)
print(age)
print(city)


# .........................Same Value.........................#

a = b = c = 10

print(a)
print(b)
print(c)


# .........................String.........................#

name = "Shyam"

print(name)
print(type(name))


# .........................Integer.........................#

age = 20

print(age)
print(type(age))


# .........................Float.........................#

height = 5.4

print(height)
print(type(height))


# .........................Boolean.........................#

is_student = True

print(is_student)
print(type(is_student))


# .........................None.........................#

x = None

print(x)
print(type(x))


# .........................List.........................#

numbers = [10, 20, 30, 40]

print(numbers)
print(type(numbers))


# .........................Tuple.........................#

numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))


# .........................Set.........................#

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))


# .........................Dictionary.........................#

student = {
    "name": "Shyam",
    "age": 20
}

print(student)
print(type(student))


# .........................Type Checking.........................#

x = 10

print(type(x))


# .........................Type Casting.........................#

x = 10

print(float(x))
print(str(x))
print(bool(x))


# .........................String to Integer.........................#

x = "100"

x = int(x)

print(x)
print(type(x))


# .........................Integer to String.........................#

x = 100

x = str(x)

print(x)
print(type(x))


# .........................Input Data Type.........................#

name = input("Enter your name: ")

print(name)
print(type(name))


# .........................Integer Input.........................#

age = int(input("Enter your age: "))

print(age)
print(type(age))


# .........................Float Input.........................#

price = float(input("Enter price: "))

print(price)
print(type(price))
