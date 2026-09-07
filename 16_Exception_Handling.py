# ===================== EXCEPTION HANDLING =====================

# .........................try except.........................#

try:
    print(10 / 0)
except:
    print("Something went wrong")


# .........................ZeroDivisionError.........................#

try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


# .........................ValueError.........................#

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input")


# .........................Multiple Exceptions.........................#

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")


# .........................else.........................#

try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print("Number =", number)


# .........................finally.........................#

try:
    print(10 / 2)

except:
    print("Error")

finally:
    print("Program Completed")


# .........................Exception as e.........................#

try:
    print(10 / 0)

except Exception as e:
    print(e)


# .........................raise.........................#

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
