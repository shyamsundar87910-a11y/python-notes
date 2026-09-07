# ===================== MODULES & PACKAGES =====================

# .........................Import Module.........................#

import math

print(math.sqrt(25))


# .........................math Module.........................#

import math

print(math.pi)
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.ceil(4.2))
print(math.floor(4.8))


# .........................from import.........................#

from math import sqrt

print(sqrt(25))


# .........................Multiple Import.........................#

from math import sqrt, pi

print(sqrt(16))
print(pi)


# .........................random Module.........................#

import random

print(random.randint(1, 10))


# .........................random Choice.........................#

import random

numbers = [10, 20, 30, 40, 50]

print(random.choice(numbers))


# .........................datetime Module.........................#

import datetime

today = datetime.date.today()

print(today)


# .........................Current Date and Time.........................#

import datetime

now = datetime.datetime.now()

print(now)


# .........................Create Own Module.........................#

# mymodule.py

def greet():
    print("Hello Python")


# .........................Import Own Module.........................#

# import mymodule

# mymodule.greet()


# .........................Module Alias.........................#

import math as m

print(m.sqrt(25))


# .........................Module Functions.........................#

import math

print(dir(math))


# .........................Package.........................#

# package/
#     __init__.py
#     calculator.py
#     operations.py


# .........................Install Package.........................#

# pip install package_name


# .........................Uninstall Package.........................#

# pip uninstall package_name
