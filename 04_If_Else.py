# ===================== IF ELSE =====================


# .........................if Statement.........................#

age = 20

if age >= 18:
    print("Adult")


# .........................if Condition.........................#

number = 10

if number > 0:
    print("Positive Number")


# .........................if else.........................#

age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# .........................if elif else.........................#

marks = 75

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("Fail")


# .........................Even or Odd.........................#

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# .........................Positive Negative.........................#

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# .........................Largest of Two Numbers.........................#

a = 10
b = 20

if a > b:
    print("a is largest")
else:
    print("b is largest")


# .........................Largest of Three Numbers.........................#

a = 10
b = 20
c = 15

if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")


# .........................Nested if.........................#

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Not Allowed")


# .........................Short Hand if.........................#

age = 20

if age >= 18: print("Adult")


# .........................Short Hand if else.........................#

age = 20

print("Adult") if age >= 18 else print("Minor")
