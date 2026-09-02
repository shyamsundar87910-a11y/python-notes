# ===================== OPERATORS =====================


# .........................Arithmetic Operators.........................#

a = 10
b = 3

print(a + b)       # Addition
print(a - b)       # Subtraction
print(a * b)       # Multiplication
print(a / b)       # Division
print(a // b)      # Floor Division
print(a % b)       # Modulus
print(a ** b)      # Exponent


# .........................Assignment Operators.........................#

x = 10

x += 5             # x = x + 5
print(x)

x -= 2             # x = x - 2
print(x)

x *= 2             # x = x * 2
print(x)

x /= 2             # x = x / 2
print(x)

x //= 2            # x = x // 2
print(x)

x %= 2             # x = x % 2
print(x)


# .........................Comparison Operators.........................#

a = 10
b = 5

print(a == b)      # Equal
print(a != b)      # Not Equal
print(a > b)       # Greater Than
print(a < b)       # Less Than
print(a >= b)      # Greater Than or Equal
print(a <= b)      # Less Than or Equal


# .........................Logical Operators.........................#

a = 10

print(a > 5 and a < 20)
print(a > 15 or a < 20)
print(not(a > 5))


# .........................Identity Operators.........................#

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)


# .........................Membership Operators.........................#

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)

print(20 not in numbers)
print(50 not in numbers)


# .........................Bitwise Operators.........................#

a = 10
b = 3

print(a & b)       # AND
print(a | b)       # OR
print(a ^ b)       # XOR
print(~a)          # NOT
print(a << 1)      # Left Shift
print(a >> 1)      # Right Shift
