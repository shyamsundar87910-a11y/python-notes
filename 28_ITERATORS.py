# .........................Basic Iterator.........................#

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# .........................Iterator with String.........................#

name = "Python"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# .........................Iterator with Tuple.........................#

numbers = (10, 20, 30, 40)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# .........................Iterator with Loop.........................#

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

for number in iterator:
    print(number)


# .........................Custom Iterator.........................#

class Numbers:

    def __init__(self, start, end):
        self.number = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.end:
            value = self.number
            self.number += 1
            return value
        else:
            raise StopIteration


numbers = Numbers(1, 5)

for number in numbers:
    print(number)


# .........................Iterator with Even Numbers.........................#

class EvenNumbers:

    def __init__(self, start, end):
        self.number = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.number <= self.end:
            value = self.number
            self.number += 1

            if value % 2 == 0:
                return value

        raise StopIteration


numbers = EvenNumbers(1, 10)

for number in numbers:
    print(number)


# .........................Iterator with List.........................#

class Student:

    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


students = Student(["Aman", "Riya", "Rahul", "Sneha"])

for student in students:
    print(student)


# .........................Iterator with String.........................#

class WordIterator:

    def __init__(self, word):
        self.word = word
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.word):
            character = self.word[self.index]
            self.index += 1
            return character
        else:
            raise StopIteration


word = WordIterator("Python")

for character in word:
    print(character)


# .........................Iterator with Multiplication Table.........................#

class Table:

    def __init__(self, number):
        self.number = number
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 10:
            result = self.number * self.count
            self.count += 1
            return result
        else:
            raise StopIteration


table = Table(5)

for result in table:
    print(result)
