# How to import module in python.

# method 1. import the whole module my name
# import csv
#csv.reader()  definition of the module

#method 2. import the whole module with an alias
#import csv as c
#c.reader()

#method 3. import one or more definitions from the module name
#from csv import reader, writer

#method 4. import all definitions with a wildcard
#from csv import reader
import csv
opened = open('potus_visitors_2015.csv', encoding='utf-8')
read_file = csv.reader(opened)
potus_data = list(read_file)
potus = potus_data[1:]
print('\n')


'''
In this mission we'll learn techniques that will allow us to:
    a. Calculate the month with the most visitors.
    b. Calculate the most common time that visits occurred.
    c. Calculate summary statistics on visit length and how far ahead visits are booked.
    d. Produce neatly formatted summaries of daily visits.
'''

import datetime as dt
eg_1 = dt.datetime(2000, 1,1)
print(eg_1)

eg_2 = dt.datetime(1985, 3, 13, 21, 26, 2)
print(eg_2)
eg_3 = dt.datetime(1998, 7, 7, 8, 39)
print(eg_3)

ibm_founded = dt.datetime(1911,6,16)
man_on_moon = dt.datetime(1969,7,20,8,17)
print(ibm_founded)
print(man_on_moon)
print('\n')

st = potus[-1][2]
print(type(st))

date_1_str = "24/12/1984"
date_1_dt = dt.datetime.strptime(date_1_str,"%d/%m/%Y")
print(date_1_dt)
date_1_str1 = "12-24-1984"
date_2_dt = dt.datetime.strptime(date_1_str1,"%m-%d-%Y")
print(date_2_dt)

'''
date_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date, date_format)
    row[2] = start_date
'''
# Using strftime() method for day/month/year format

dt_object = dt.datetime(1984, 12,24)
dt_string = dt_object.strftime("%d/%m/%Y")
print(dt_string)

dt_string = dt_object.strftime("%B, %d, %Y")
print("this is", dt_string)

dt_string = dt_object.strftime("%A %B %d at 1:%M %p")
print(dt_string)
print(" ")


'''
visitors_per_month = {}
for row in potus:
    month_dt = row[2]
    month_str = month_dt.strftime("%B,%Y")
    if month_str not in visitors_per_month:
        visitors_per_month[month_str] = 1
    else:
        visitors_per_month[month_str] += 1

print(visitors_per_month)
'''

