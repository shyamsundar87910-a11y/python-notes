# ===================== 35_LIST_COMPREHENSION.py =====================


# .........................Basic List Comprehension.........................#

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# .........................List Comprehension with Range.........................#

numbers = [number for number in range(1, 6)]

print(numbers)


# .........................List Comprehension with Condition.........................#

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# .........................List Comprehension with Odd Numbers.........................#

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = [number for number in numbers if number % 2 != 0]

print(odd_numbers)


# .........................List Comprehension with if else.........................#

numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(result)


# .........................List Comprehension with String.........................#

names = ["aman", "rahul", "riya"]

upper_names = [name.upper() for name in names]

print(upper_names)


# .........................List Comprehension with String Length.........................#

names = ["Aman", "Rahul", "Riya", "Shyam"]

lengths = [len(name) for name in names]

print(lengths)


# .........................List Comprehension with Multiplication.........................#

numbers = [1, 2, 3, 4, 5]

double = [number * 2 for number in numbers]

print(double)


# .........................List Comprehension with Nested Loop.........................#

numbers = [1, 2, 3]

result = [number * 2 for number in numbers for i in range(2)]

print(result)


# .........................List Comprehension with Multiple Conditions.........................#

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [number for number in numbers if number > 5 and number % 2 == 0]

print(result)
