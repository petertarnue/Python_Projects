
opened = open("AppleStone - goog4_request&X-Goog-Date=20210114T104926Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=29e5b444bd18b7149d5a341fb65d8e8a02e60c4e05444601eb367fb91605626139559cae29b5293fe85bbfe5fc5e740f997775b33bd9834b9863b84.csv",
    encoding="utf-8")
from csv import reader
word = reader(opened)
appData = list(word)

handel = open('AppleStone11.csv')


content_rating = {}
for row in appData[1:]:
    c_rating = row[11]
    if c_rating in content_rating:
        content_rating[c_rating] += 1
    else:
        content_rating[c_rating] = 1
# print('The histogram is: ', content_rating)

for row in appData[1:]:
    c_r = (row[11])
    content_rating[c_r] = content_rating.get(c_r, 0) + 1
print('the frequency is: ', content_rating)


def square(number):
    result = number * number
    return result


print(square(10))


def add_10(value):
    return value + 10


add_30 = add_10(30)
add_90 = add_10(90)
print(add_90)
print(add_30)


# Function Definitions

def extract(index):
    column = []
    for row in appData[1:]:
        value = row[index]
        column.append(value)
    return column

p1 = extract(6)
#print(p1)

def collect(C):
    collumers = []
    for x in appData[1:]:
        row2 = x[C]
        collumers.append(row2)
    return collumers


cont_rating = collect(11)
#print(p40)

# Defining a function for getting the frequency of data in column
# of a dataset
def freq_table(column):
    frequency_table = {}
    for value in column:
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table



cont_rating_ft = freq_table(cont_rating)
#print('content rating frequency is: ', cont_rating_ft)

# Finding the frequency of the particular data point of column
# in a data set directly
def histog(value):
    hist_dict = {}
    for x in appData[1:]:
        colum_row = x[value]
        if colum_row in hist_dict:
            hist_dict[colum_row] += 1
        else:
            hist_dict[colum_row] = 1
    return hist_dict

content_r = histog(11)
print(content_r)

# Finding the frequency of the particular data point of column
# a data set


def peterlove(eve):
    joeDict = {}
    for row in appData[1:]:
        pe = row[eve]
        if pe in joeDict:
            joeDict[pe] += 1
        else:
            joeDict[pe] = 1
    return joeDict

p40 = peterlove(11)
print(p40)

print(" ")

# This function get the frequency of any data point in column
# of a dataset.
def frequ_table(data_set, c_ind):
    frequenci = {}
    for row in data_set[1:]:
        row_value = row[c_ind]
        if row_value in frequenci:
            frequenci[row_value] += 1
        else:
            frequenci[row_value] = 1
    return frequenci

# Examples of positional argument and key word arguments

contRating = frequ_table(data_set= appData,c_ind= 11)
print(contRating)
print('')
userRating = frequ_table(data_set=appData, c_ind= 8)
print(' ')
print(userRating)
print(' ')
genre_ft = frequ_table(appData, c_ind= 12)
print(genre_ft)

# Nesting functions in the body of another function


def extractcolumn(dataset, index):
    column = []
    for x in appData[1:]:
        value = x[index]
        column.append(value)
    return column


def find_sum(a_list):
    a_sum = 0
    for elements in a_list:
        a_sum += float(elements)
    return a_sum


def find_length(alist):
    length = 0
    for elemn  in alist:
        length += 1
    return length


def mean(dataset, index):
    column = extractcolumn(dataset, index)
    return find_sum(column) / find_length(column)


avg_price = mean(appData, 5)
print(avg_price)
