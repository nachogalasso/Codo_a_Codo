# 30 Days Of Python: Day 16 - Python Date time


"""
Day 16
Python datetime
Python has got datetime module to handle date and time.

import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on date, datetime, time and timedelta. Let se see them one by one.

Getting datetime Information

"""

from datetime import datetime, date, time, timedelta

# print(dir(datetime))
today = datetime.now()
print(type(today))
print(today)

# Let's use the datetime and put the diferent values into variables
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
seconds = today.second
timestamp = today.timestamp()
print(day, month, year, hour, minute, seconds)
print('The timestamp is: ', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}:{seconds}')

"""Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC."""

new_year = datetime(2024, 1, 1)
# When we use datetime(2024, 1, 1) we format the date as we establish in the ()
print(new_year)
day1 = new_year.day
month1 = new_year.month
year1 = new_year.year
hour1 = new_year.hour
minute1 = new_year.minute
seconds1 = new_year.second
print(day1, month1, year1, hour1, minute1, seconds1)
print(f'{day1}-{month1}-{year1} => {hour1}:{minute1}:{seconds1}')

# Formatting Date Output Using strftime
# https://strftime.org/

# We can format the date using the strftime and establish the way we want to see the date
date_with_strftime = datetime.now()
t = date_with_strftime.strftime("%H:%M:%S") # I will have the hour time with the format indicated
print('The time is: ', t)
# Now we can add the date
time_one = date_with_strftime.strftime("%d/%m/%y, %H:%M:%S")
print(time_one)
time_two = date_with_strftime.strftime("%m/%d/%y, %H:%M:%S")
print(time_two)

"""
String to Time Using strptime

We can use a date string to create our time using strptime
"""
date_string = '9 de October, 2024' # Because I use 'de' I received a valuerror, we need to write the
# date with out using other strings. Also I'm required to write the dates in english
date_string1 = '09 October, 2024'
print("date string: ", date_string)
# Now we use strptime to format the string date
date_object = datetime.strptime(date_string1, "%d %B, %Y")
print(date_object)

"""Using date from datetime"""

d = date(2024, 1, 1)
print(d)
# If we want use the corrent date we need to use the today() method
print('Today is: ', d.today()) # The date will be expressed in first year-month-date
today1 = date.today()
print(type(today1))
# Because today is a spcial date or object type, we can access to the different values in it
print('Current year: ', today1.year)
print('Current month: ', today1.month)
print('Current day: ', today1.day)
# We can desconstruc the date into pieces

"""Time Objects to Represent Time"""

# time(hour = 0, minute = 0, second = 0)
a = time() # The time will be 00:00:00 but we can format or tell which is, comes first hour, min, sec
print(a)
b = time(hour=16, minute=17, second=32)
print(b)
# We can also write
c = time(16, 22, 35)
print('The time is: ', c)
""" If we need we can add the microseconds
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
"""

"""Difference Between Two Points in Time Using"""
# We can establish a date and then we can later use it to calculate time elapsed or time left

today = date(year=2024, month=10, day=7)
new_year = date(year=2025, month=1, day=1)
timeleft_for_newyear = new_year - today
print(timeleft_for_newyear)

# We can also use it with the hours
t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2024, month = 10, day = 7, hour = 16, minute = 52, second = 12)
diff = t2 - t1
print('Time left for new year:', diff)

"""Difference Between Two Points in Time Using timedelata"""

t4 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t5 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t6 = t4 - t5
print("t6 =", t6)


# EXERCISES

#1
today_current_date = datetime.now()
print("today_current_date =", today_current_date)
today_timestamp = today_current_date.timestamp()
print(today_timestamp)

#2
date_format = today_current_date.strftime("%m/%d/%Y, %H:%M:%S")
print(date_format)

#3
s_to_d = '7 October, 2024'
s_to_d_object = datetime.strptime(s_to_d, "%d %B, %Y")
print(s_to_d_object)

#5
fst_date = date(year=1970, month=1, day=1)
sd_date = date(year=2024, month=10, day=7)
diff_date = sd_date - fst_date
print(diff_date)