# ===================== RECURSION =====================

# .........................Basic Recursion.........................#

def count(n):

    if n == 0:
        return

    print(n)

    count(n - 1)


count(5)


# .........................Countdown.........................#

def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)


countdown(5)


# .........................Count Up.........................#

def countup(n):

    if n == 0:
        return

    countup(n - 1)

    print(n)


countup(5)


# .........................Factorial.........................#

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# .........................Sum of Numbers.........................#

def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)


print(total(5))


# .........................Fibonacci.........................#

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


# .........................Print Fibonacci Series.........................#

def fibonacci_series(n):

    if n <= 1:
        return n

    return fibonacci_series(n - 1) + fibonacci_series(n - 2)


for i in range(10):
    print(fibonacci_series(i))


# .........................Power.........................#

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print(power(2, 5))


# .........................Reverse String.........................#

def reverse(text):

    if text == "":
        return ""

    return reverse(text[1:]) + text[0]


print(reverse("Python"))


# .........................Recursion with List.........................#

def print_list(numbers, index=0):

    if index == len(numbers):
        return

    print(numbers[index])

    print_list(numbers, index + 1)


numbers = [10, 20, 30, 40, 50]

print_list(numbers)
