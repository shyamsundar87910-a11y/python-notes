# ===================== LOOPS =====================


# .........................for Loop.........................#

for i in range(5):
    print(i)


# .........................range().........................#

for i in range(1, 6):
    print(i)


# .........................Print Numbers.........................#

for i in range(1, 11):
    print(i)


# .........................Print Even Numbers.........................#

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# .........................Print Odd Numbers.........................#

for i in range(1, 11):
    if i % 2 != 0:
        print(i)


# .........................List with for Loop.........................#

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# .........................String with for Loop.........................#

name = "Python"

for char in name:
    print(char)


# .........................while Loop.........................#

i = 1

while i <= 5:
    print(i)
    i += 1


# .........................Reverse while Loop.........................#

i = 5

while i >= 1:
    print(i)
    i -= 1


# .........................break.........................#

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# .........................continue.........................#

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# .........................pass.........................#

for i in range(5):
    pass


# .........................Nested Loop.........................#

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# .........................Multiplication Table.........................#

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# .........................Sum of Numbers.........................#

total = 0

for i in range(1, 11):
    total += i

print(total)


# .........................Factorial.........................#

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(factorial)


# .........................for else.........................#

for i in range(5):
    print(i)
else:
    print("Loop Completed")


# .........................while else.........................#

i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop Completed")
