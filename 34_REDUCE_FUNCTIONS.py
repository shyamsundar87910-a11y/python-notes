# ===================== 34_REDUCE_FUNCTIONS.py =====================

from functools import reduce


# .........................Basic Reduce.........................#

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)


# .........................Reduce with Multiplication.........................#

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a * b, numbers)

print(result)


# .........................Reduce with Maximum Value.........................#

numbers = [10, 50, 30, 80, 20]

result = reduce(lambda a, b: a if a > b else b, numbers)

print(result)


# .........................Reduce with Minimum Value.........................#

numbers = [10, 50, 30, 80, 20]

result = reduce(lambda a, b: a if a < b else b, numbers)

print(result)
