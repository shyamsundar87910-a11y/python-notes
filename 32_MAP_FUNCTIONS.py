# ===================== 32_MAP_FUNCTIONS.py =====================


# .........................Basic Map.........................#

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)


# .........................Map with Square.........................#

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)


# .........................Map with String.........................#

names = ["aman", "rahul", "riya"]

result = list(map(lambda name: name.upper(), names))

print(result)


# .........................Map with Addition.........................#

numbers1 = [10, 20, 30]
numbers2 = [1, 2, 3]

result = list(map(lambda a, b: a + b, numbers1, numbers2))

print(result)
