# ===================== FILE HANDLING =====================

# .........................Create File.........................#

file = open("data.txt", "w")

file.write("Hello Python")

file.close()


# .........................Read File.........................#

file = open("data.txt", "r")

data = file.read()

print(data)

file.close()


# .........................Write File.........................#

file = open("data.txt", "w")

file.write("Python Data Analytics")

file.close()


# .........................Append File.........................#

file = open("data.txt", "a")

file.write("\nPandas")

file.close()


# .........................Read Lines.........................#

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# .........................with open.........................#

with open("data.txt", "r") as file:

    data = file.read()

    print(data)


# .........................Write Multiple Lines.........................#

with open("data.txt", "w") as file:

    file.write("Python\n")
    file.write("Pandas\n")
    file.write("NumPy\n")


# .........................Read Multiple Lines.........................#

with open("data.txt", "r") as file:

    for line in file:
        print(line.strip())


# .........................File Modes.........................#

# r = Read
# w = Write
# a = Append
# x = Create
