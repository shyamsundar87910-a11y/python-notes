# ===================== FILE HANDLING =====================

# .........................Open File.........................#

file = open("data.txt", "r")

print(file)


# .........................Read File.........................#

file = open("data.txt", "r")

data = file.read()

print(data)

file.close()


# .........................Write File.........................#

file = open("data.txt", "w")

file.write("Hello Python")

file.close()


# .........................Append File.........................#

file = open("data.txt", "a")

file.write("\nPython Data Analytics")

file.close()


# .........................Read Lines.........................#

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# .........................Read One Line.........................#

file = open("data.txt", "r")

line = file.readline()

print(line)

file.close()


# .........................Read Multiple Lines.........................#

file = open("data.txt", "r")

for line in file:
    print(line.strip())

file.close()


# .........................with open.........................#

with open("data.txt", "r") as file:
    data = file.read()

print(data)


# .........................Write Multiple Lines.........................#

with open("data.txt", "w") as file:
    file.write("Python\n")
    file.write("NumPy\n")
    file.write("Pandas\n")


# .........................Append Multiple Lines.........................#

with open("data.txt", "a") as file:
    file.write("Matplotlib\n")
    file.write("Seaborn\n")


# .........................File Exists Check.........................#

import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")


# .........................Delete File.........................#

import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("File does not exist")


# .........................File Modes.........................#

# r = Read
# w = Write
# a = Append
# x = Create
# b = Binary
# t = Text
