# ===================== 41_JSON.py =====================


# .........................Import JSON.........................#

import json


# .........................Python Dictionary to JSON.........................#

student = {
    "name": "Shyam",
    "age": 21,
    "course": "BCA"
}

data = json.dumps(student)

print(data)


# .........................JSON to Python Dictionary.........................#

data = '{"name": "Shyam", "age": 21, "course": "BCA"}'

student = json.loads(data)

print(student)
print(student["name"])


# .........................JSON List.........................#

data = '["Python", "Pandas", "NumPy", "SQL"]'

skills = json.loads(data)

print(skills)


# .........................Access JSON Data.........................#

data = '{"name": "Shyam", "marks": 85}'

student = json.loads(data)

print(student["name"])
print(student["marks"])


# .........................Pretty JSON.........................#

student = {
    "name": "Shyam",
    "age": 21,
    "course": "BCA"
}

data = json.dumps(student, indent=4)

print(data)


# .........................JSON with Multiple Students.........................#

students = [
    {"name": "Shyam", "marks": 85},
    {"name": "Rahul", "marks": 90},
    {"name": "Aman", "marks": 78}
]

data = json.dumps(students, indent=4)

print(data)
