# ===================== LISTS =====================


# .........................Creating List.........................#

numbers = [10, 20, 30, 40, 50]

print(numbers)


# .........................Different Data Types.........................#

data = ["Shyam", 20, 5.4, True]

print(data)


# .........................List Length.........................#

numbers = [10, 20, 30, 40, 50]

print(len(numbers))


# .........................Indexing.........................#

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])


# .........................Slicing.........................#

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])


# .........................Change Item.........................#

numbers = [10, 20, 30, 40]

numbers[1] = 100

print(numbers)


# .........................Add Item - append().........................#

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


# .........................Add Item - insert().........................#

numbers = [10, 20, 30]

numbers.insert(1, 100)

print(numbers)


# .........................Add Multiple Items - extend().........................#

numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)


# .........................Remove Item - remove().........................#

numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)


# .........................Remove Item - pop().........................#

numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)


# Remove using Index

numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)


# .........................Delete Item.........................#

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)


# .........................Clear List.........................#

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


# .........................Check Item.........................#

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)


# .........................Count.........................#

numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))


# .........................Index.........................#

numbers = [10, 20, 30, 40]

print(numbers.index(30))


# .........................Sort.........................#

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)


# .........................Reverse.........................#

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)


# .........................Copy.........................#

numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(new_numbers)


# .........................Join Lists.........................#

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)


# .........................Loop Through List.........................#

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# .........................List Comprehension.........................#

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)


# .........................Even Numbers.........................#

numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x % 2 == 0]

print(even)
