# ===================== 40_REGEX.py =====================


# .........................Import Regex.........................#

import re


# .........................Basic Search.........................#

text = "I am learning Python"

result = re.search("Python", text)

print(result)


# .........................Find All.........................#

text = "Python is easy. Python is powerful."

result = re.findall("Python", text)

print(result)


# .........................Find Numbers.........................#

text = "My marks are 85 and 90"

numbers = re.findall("[0-9]+", text)

print(numbers)


# .........................Find Words Starting with P.........................#

text = "Python Pandas NumPy Programming"

words = re.findall(r"\bP\w+", text)

print(words)


# .........................Replace Text.........................#

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)


# .........................Check Email Pattern.........................#

email = "student@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

result = re.match(pattern, email)

print(result)


# .........................Find Capital Letters.........................#

text = "Python Data Analytics"

result = re.findall("[A-Z]", text)

print(result)


# .........................Find Small Letters.........................#

text = "Python Data Analytics"

result = re.findall("[a-z]", text)

print(result)
