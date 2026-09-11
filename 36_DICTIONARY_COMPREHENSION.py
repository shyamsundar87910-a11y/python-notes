# ===================== 36_DICTIONARY_COMPREHENSION.py =====================


# .........................Basic Dictionary Comprehension.........................#

numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)


# .........................Dictionary Comprehension with Range.........................#

numbers = range(1, 6)

result = {number: number * 2 for number in numbers}

print(result)


# .........................Dictionary Comprehension with Condition.........................#

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)


# .........................Dictionary Comprehension with if else.........................#

numbers = [1, 2, 3, 4, 5]

result = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}

print(result)


# .........................Dictionary Comprehension with Strings.........................#

names = ["Aman", "Rahul", "Riya"]

result = {name: len(name) for name in names}

print(result)


# .........................Dictionary Comprehension with Uppercase.........................#

names = ["aman", "rahul", "riya"]

result = {name: name.upper() for name in names}

print(result)


# .........................Dictionary Comprehension from Two Lists.........................#

names = ["Aman", "Rahul", "Riya"]
marks = [80, 75, 90]

result = {
    name: mark
    for name, mark in zip(names, marks)
}

print(result)


# .........................Dictionary Comprehension with Calculation.........................#

numbers = [10, 20, 30, 40]

result = {
    number: number + 5
    for number in numbers
}

print(result)


# .........................Dictionary Comprehension with Multiple Conditions.........................#

numbers = range(1, 11)

result = {
    number: number ** 2
    for number in numbers
    if number > 5 and number % 2 == 0
}

print(result)


# .........................Dictionary Comprehension from Dictionary.........................#

students = {
    "Aman": 80,
    "Rahul": 65,
    "Riya": 90
}

result = {
    name: marks
    for name, marks in students.items()
    if marks >= 70
}

print(result)
