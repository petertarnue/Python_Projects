opened = open(
    'AppleStone - goog4_request&X-Goog-Date=20210114T104926Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=29e5b444bd18b7149d5a341fb65d8e8a02e60c4e05444601eb367fb91605626139559cae29b5293fe85bbfe5fc5e740f997775b33bd9834b9863b84.csv',
    encoding='utf-8')
from csv import reader

word_file = reader(opened)
data = list(word_file)


def opened_file(file_name):
    try:
        opened = open(file_name)
        from csv import reader
        read_file = reader(opened)
        real_dataset = list(read_file)
        return real_dataset
    except:
        print("nothing is happening here."
              "please check your file name,"
              "and retype it correctly.")



def open_dataset(file_name):
    opened_f = open(file_name)
    from csv import reader
    read_file = reader(opened_f)
    dataMove = list(read_file)
    return dataMove


def ope_data(data_file, header=True):
    ope = open(data_file)
    from csv import reader
    woo = reader(ope)
    dataAP = list(woo)
    if header:
        return dataAP[1:], dataAP[0]
    else:
        return dataAP


def value_sum(p=4, e=9):
    sum3 = p + e
    difference2 = p - e
    return sum3, difference2


print(value_sum(50, 5))

e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e ** x


result = exponential(5)
print(result)


def divide():
    print(5)
    print(length)
    return a_sum / length


result_2 = divide()
print(result_2)

