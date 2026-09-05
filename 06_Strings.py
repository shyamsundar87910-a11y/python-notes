# ===================== STRINGS =====================


# .........................Creating String.........................#

name = "Shyam"

print(name)


# .........................Single Quotes.........................#

name = 'Shyam'

print(name)


# .........................Double Quotes.........................#

name = "Shyam"

print(name)


# .........................Triple Quotes.........................#

text = """Python
is
easy"""

print(text)


# .........................String Length.........................#

name = "Python"

print(len(name))


# .........................Indexing.........................#

name = "Python"

print(name[0])
print(name[1])
print(name[-1])
print(name[-2])


# .........................Slicing.........................#

name = "Python"

print(name[0:3])
print(name[2:6])
print(name[:4])
print(name[2:])
print(name[:])


# .........................Reverse String.........................#

name = "Python"

print(name[::-1])


# .........................String Concatenation.........................#

first_name = "Shyam"
last_name = "Sundar"

full_name = first_name + " " + last_name

print(full_name)


# .........................String Repetition.........................#

text = "Python "

print(text * 3)


# .........................Membership.........................#

text = "Python"

print("P" in text)
print("z" in text)

print("P" not in text)


# .........................upper().........................#

name = "python"

print(name.upper())


# .........................lower().........................#

name = "PYTHON"

print(name.lower())


# .........................capitalize().........................#

name = "python"

print(name.capitalize())


# .........................title().........................#

name = "python programming"

print(name.title())


# .........................swapcase().........................#

name = "Python Programming"

print(name.swapcase())


# .........................strip().........................#

name = "  Python  "

print(name.strip())


# .........................lstrip().........................#

name = "  Python"

print(name.lstrip())


# .........................rstrip().........................#

name = "Python  "

print(name.rstrip())


# .........................replace().........................#

text = "I like Java"

print(text.replace("Java", "Python"))


# .........................split().........................#

text = "Python is easy"

print(text.split())


# .........................join().........................#

words = ["Python", "is", "easy"]

print(" ".join(words))


# .........................find().........................#

text = "Python Programming"

print(text.find("Programming"))


# .........................count().........................#

text = "banana"

print(text.count("a"))


# .........................startswith().........................#

text = "Python Programming"

print(text.startswith("Python"))


# .........................endswith().........................#

text = "Python Programming"

print(text.endswith("Programming"))


# .........................isdigit().........................#

text = "12345"

print(text.isdigit())


# .........................isalpha().........................#

text = "Python"

print(text.isalpha())


# .........................isalnum().........................#

text = "Python123"

print(text.isalnum())


# .........................isspace().........................#

text = "   "

print(text.isspace())


# .........................String Formatting.........................#

name = "Shyam"
age = 20

print(f"My name is {name} and I am {age} years old.")


# .........................Escape Characters.........................#

print("Hello\nWorld")

print("Hello\tWorld")

print("He said \"Hello\"")


# .........................String Comparison.........................#

a = "Python"
b = "Python"

print(a == b)


# .........................Input String.........................#

name = input("Enter your name: ")

print(name)


# .........................Reverse Input String.........................#

name = input("Enter your name: ")

print(name[::-1])
