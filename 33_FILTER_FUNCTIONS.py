# ===================== 33_FILTER_FUNCTIONS.py =====================


# .........................Basic Filter.........................#

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)


# .........................Filter Odd Numbers.........................#

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 != 0, numbers))

print(result)


# .........................Filter Greater Numbers.........................#

numbers = [10, 20, 30, 40, 50]

result = list(filter(lambda x: x > 25, numbers))

print(result)


# .........................Filter String.........................#

names = ["Aman", "Rahul", "Riya", "Raj"]

result = list(filter(lambda name: len(name) > 3, names))

print(result)
