# ===================== 39_ITERABLES.py =====================


# .........................List Iterable.........................#

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# .........................String Iterable.........................#

name = "Python"

for letter in name:
    print(letter)


# .........................Tuple Iterable.........................#

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# .........................Dictionary Iterable.........................#

student = {
    "name": "Shyam",
    "age": 21,
    "course": "BCA"
}

for key in student:
    print(key)


# .........................Dictionary Values.........................#

for value in student.values():
    print(value)


# .........................Dictionary Items.........................#

for key, value in student.items():
    print(key, value)


# .........................Set Iterable.........................#

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)


# .........................Range Iterable.........................#

for number in range(1, 6):
    print(number)


# .........................Checking Iterable with iter().........................#

numbers = [10, 20, 30]

data = iter(numbers)

print(next(data))
print(next(data))
print(next(data))
