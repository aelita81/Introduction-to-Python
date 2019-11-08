import datetime
import calendar
import time
bday = datetime.date(1981, 12, 20)
print(bday)
print(bday.year)
print(bday.month)
print(bday.day)
print(bday.isoweekday())
today = datetime.date.today()
date1 = datetime.datetime(2019, 12, 20)
date2 = datetime.datetime.today()
date3 = date1 - date2
print(date3)
cal = calendar.month(2017, 5)
print(cal)
now=datetime.datetime.now()
delta = datetime.timedelta(days = 1)
y=now - delta
print(y)
delta2 = datetime.timedelta(days = 2)
print(y+ delta2)
delta3 = datetime.timedelta(days = 3)
print(y- delta3)