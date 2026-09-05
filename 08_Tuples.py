# ===================== TUPLES =====================


# .........................Creating Tuple.........................#

numbers = (10, 20, 30, 40, 50)

print(numbers)


# .........................Different Data Types.........................#

data = ("Shyam", 20, 5.4, True)

print(data)


# .........................Single Item Tuple.........................#

x = (10,)

print(x)
print(type(x))


# .........................Tuple Length.........................#

numbers = (10, 20, 30, 40, 50)

print(len(numbers))


# .........................Indexing.........................#

numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[2])
print(numbers[-1])


# .........................Slicing.........................#

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])


# .........................Tuple is Immutable.........................#

numbers = (10, 20, 30)

# numbers[0] = 100     # Error

print(numbers)


# .........................Check Item.........................#

numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 in numbers)


# .........................Count.........................#

numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))


# .........................Index.........................#

numbers = (10, 20, 30, 40)

print(numbers.index(30))


# .........................Loop Through Tuple.........................#

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# .........................Tuple Concatenation.........................#

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2

print(tuple3)


# .........................Tuple Repetition.........................#

numbers = (1, 2, 3)

print(numbers * 2)


# .........................Nested Tuple.........................#

data = ((1, 2), (3, 4), (5, 6))

print(data)

print(data[0])
print(data[1][1])


# .........................Tuple Unpacking.........................#

data = ("Shyam", 20, "BCA")

name, age, course = data

print(name)
print(age)
print(course)


# .........................Convert List to Tuple.........................#

numbers = [10, 20, 30, 40]

numbers = tuple(numbers)

print(numbers)


# .........................Convert Tuple to List.........................#

numbers = (10, 20, 30, 40)

numbers = list(numbers)

print(numbers)


# .........................max().........................#

numbers = (10, 20, 30, 40)

print(max(numbers))


# .........................min().........................#

numbers = (10, 20, 30, 40)

print(min(numbers))


# .........................sum().........................#

numbers = (10, 20, 30, 40)

print(sum(numbers))
