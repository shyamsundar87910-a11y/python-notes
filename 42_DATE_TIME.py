# ===================== 42_DATE_TIME.py =====================


# .........................Import DateTime.........................#

from datetime import datetime


# .........................Current Date and Time.........................#

now = datetime.now()

print(now)


# .........................Current Date.........................#

today = datetime.now().date()

print(today)


# .........................Current Time.........................#

time = datetime.now().time()

print(time)


# .........................Specific Date.........................#

date = datetime(2026, 9, 13)

print(date)


# .........................Date Formatting.........................#

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%B"))
print(now.strftime("%A"))


# .........................Create Date and Time.........................#

date_time = datetime(2026, 9, 13, 8, 30)

print(date_time)


# .........................Date Difference.........................#

date1 = datetime(2026, 9, 10)
date2 = datetime(2026, 9, 13)

difference = date2 - date1

print(difference.days)


# .........................Extract Date Information.........................#

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
