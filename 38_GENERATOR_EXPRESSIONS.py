# ===================== 38_GENERATOR_EXPRESSIONS.py =====================


# .........................Basic Generator Expression.........................#

numbers = (x for x in range(1, 6))

for number in numbers:
    print(number)


# .........................Square Generator Expression.........................#

squares = (x * x for x in range(1, 6))

for square in squares:
    print(square)


# .........................Even Numbers.........................#

even_numbers = (x for x in range(1, 11) if x % 2 == 0)

for number in even_numbers:
    print(number)


# .........................Odd Numbers.........................#

odd_numbers = (x for x in range(1, 11) if x % 2 != 0)

for number in odd_numbers:
    print(number)


# .........................String Generator Expression.........................#

names = ["Shyam", "Rahul", "Aman", "Ravi"]

name_length = (len(name) for name in names)

for length in name_length:
    print(length)


# .........................Uppercase Generator Expression.........................#

names = ["python", "pandas", "numpy"]

upper_names = (name.upper() for name in names)

for name in upper_names:
    print(name)


# .........................Generator with Condition.........................#

numbers = (x * 2 for x in range(1, 11) if x > 5)

for number in numbers:
    print(number)


# .........................Sum Using Generator Expression.........................#

numbers = (x for x in range(1, 6))

total = sum(numbers)

print(total)


# .........................Maximum Using Generator Expression.........................#

numbers = (x for x in range(1, 11))

maximum = max(numbers)

print(maximum)
