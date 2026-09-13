# ===================== 43_CSV.py =====================


# .........................Import CSV.........................#

import csv


# .........................Write CSV File.........................#

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Shyam", 21, 85])
    writer.writerow(["Rahul", 20, 90])
    writer.writerow(["Aman", 21, 78])


# .........................Read CSV File.........................#

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# .........................Read CSV Rows.........................#

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0], row[2])


# .........................Dictionary CSV.........................#

students = [
    {"Name": "Shyam", "Age": 21, "Marks": 85},
    {"Name": "Rahul", "Age": 20, "Marks": 90}
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)


# .........................Read Dictionary CSV.........................#

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], row["Marks"])
