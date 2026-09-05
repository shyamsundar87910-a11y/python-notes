# ===================== SETS =====================


# .........................Creating Set.........................#

numbers = {10, 20, 30, 40, 50}

print(numbers)


# .........................Duplicate Values.........................#

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)


# .........................Different Data Types.........................#

data = {"Shyam", 20, 5.4, True}

print(data)


# .........................Set Length.........................#

numbers = {10, 20, 30, 40}

print(len(numbers))


# .........................Check Item.........................#

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(50 in numbers)


# .........................Add Item - add().........................#

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)


# .........................Add Multiple Items - update().........................#

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)


# .........................Remove Item - remove().........................#

numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)


# .........................Remove Item - discard().........................#

numbers = {10, 20, 30, 40}

numbers.discard(30)

print(numbers)


# .........................Remove Random Item - pop().........................#

numbers = {10, 20, 30, 40}

numbers.pop()

print(numbers)


# .........................Clear Set.........................#

numbers = {10, 20, 30}

numbers.clear()

print(numbers)


# .........................Delete Set.........................#

numbers = {10, 20, 30}

del numbers


# .........................Loop Through Set.........................#

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)


# .........................Union.........................#

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))


# .........................Intersection.........................#

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))


# .........................Difference.........................#

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.difference(set2))


# .........................Symmetric Difference.........................#

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.symmetric_difference(set2))


# .........................Subset.........................#

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))


# .........................Superset.........................#

set1 = {1, 2, 3, 4}
set2 = {1, 2}

print(set1.issuperset(set2))


# .........................Disjoint.........................#

set1 = {1, 2}
set2 = {3, 4}

print(set1.isdisjoint(set2))


# .........................Set from List.........................#

numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)

print(unique_numbers)


# .........................Set to List.........................#

numbers = {10, 20, 30, 40}

numbers = list(numbers)

print(numbers)
