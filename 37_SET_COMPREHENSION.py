# ===================== 37_SET_COMPREHENSION.py =====================


# .........................Basic Set Comprehension.........................#

numbers = [1, 2, 3, 4, 5]

squares = {number ** 2 for number in numbers}

print(squares)


# .........................Set Comprehension with Range.........................#

numbers = range(1, 6)

result = {number * 2 for number in numbers}

print(result)


# .........................Set Comprehension with Condition.........................#

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)


# .........................Set Comprehension with Odd Numbers.........................#

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = {
    number
    for number in numbers
    if number % 2 != 0
}

print(odd_numbers)


# .........................Set Comprehension with if else.........................#

numbers = [1, 2, 3, 4, 5]

result = {
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}

print(result)


# .........................Set Comprehension with String.........................#

name = "Python"

letters = {letter for letter in name}

print(letters)


# .........................Set Comprehension with Uppercase.........................#

names = ["aman", "rahul", "riya"]

result = {name.upper() for name in names}

print(result)


# .........................Set Comprehension with Calculation.........................#

numbers = [10, 20, 30, 40]

result = {number + 5 for number in numbers}

print(result)


# .........................Set Comprehension with Multiple Conditions.........................#

numbers = range(1, 11)

result = {
    number
    for number in numbers
    if number > 5 and number % 2 == 0
}

print(result)


# .........................Duplicate Values.........................#

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

result = {number for number in numbers}

print(result)
