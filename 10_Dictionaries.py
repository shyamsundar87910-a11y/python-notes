# ===================== DICTIONARIES =====================

# .........................Creating Dictionary.........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

print(student)


# .........................Access Item.........................#

student = {
    "name": "Shyam",
    "age": 20
}

print(student["name"])
print(student["age"])


# .........................get().........................#

student = {
    "name": "Shyam",
    "age": 20
}

print(student.get("name"))
print(student.get("age"))


# .........................Check Key.........................#

student = {
    "name": "Shyam",
    "age": 20
}

print("name" in student)
print("city" in student)


# .........................Add Item.........................#

student = {
    "name": "Shyam",
    "age": 20
}

student["city"] = "Jamshedpur"

print(student)


# .........................Change Item.........................#

student = {
    "name": "Shyam",
    "age": 20
}

student["age"] = 21

print(student)


# .........................update().........................#

student = {
    "name": "Shyam",
    "age": 20
}

student.update({"city": "Jamshedpur"})

print(student)


# .........................Dictionary Length.........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

print(len(student))


# .........................keys().........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

print(student.keys())


# .........................values().........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

print(student.values())


# .........................items().........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

print(student.items())


# .........................Remove Item - pop().........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

student.pop("age")

print(student)


# .........................Remove Last Item - popitem().........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

student.popitem()

print(student)


# .........................Delete Item.........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

del student["age"]

print(student)


# .........................Clear Dictionary.........................#

student = {
    "name": "Shyam",
    "age": 20
}

student.clear()

print(student)


# .........................Delete Dictionary.........................#

student = {
    "name": "Shyam",
    "age": 20
}

del student


# .........................Loop Through Keys.........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

for key in student:
    print(key)


# .........................Loop Through Values.........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

for value in student.values():
    print(value)


# .........................Loop Through Items.........................#

student = {
    "name": "Shyam",
    "age": 20,
    "course": "BCA"
}

for key, value in student.items():
    print(key, value)


# .........................Copy Dictionary.........................#

student = {
    "name": "Shyam",
    "age": 20
}

new_student = student.copy()

print(new_student)


# .........................Nested Dictionary.........................#

students = {
    "student1": {
        "name": "Shyam",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students)


# .........................Access Nested Dictionary.........................#

students = {
    "student1": {
        "name": "Shyam",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students["student1"]["name"])
print(students["student2"]["age"])


# .........................Dictionary with List.........................#

student = {
    "name": "Shyam",
    "marks": [80, 85, 90]
}

print(student)
print(student["marks"])


# .........................Dictionary Comprehension.........................#

numbers = [1, 2, 3, 4, 5]

squares = {x: x ** 2 for x in numbers}

print(squares)


# .........................Even Numbers Dictionary.........................#

numbers = [1, 2, 3, 4, 5, 6]

even = {x: x ** 2 for x in numbers if x % 2 == 0}

print(even)


# .........................Dictionary from Two Lists.........................#

keys = ["name", "age", "city"]
values = ["Shyam", 20, "Jamshedpur"]

student = dict(zip(keys, values))

print(student)


# .........................Input Dictionary.........................#

name = input("Enter your name: ")
age = int(input("Enter your age: "))

student = {
    "name": name,
    "age": age
}

print(student)
