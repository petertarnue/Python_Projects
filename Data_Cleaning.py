from csv import reader
opened_file = open('artworks_final.csv.', encoding='utf-8')
read_file = reader(opened_file)
moma = list(read_file)
#print(moma[1:])


'''
Using the str.replace() method to remove symbols or string that 
we don't want in a column of a dataset.
'''
name = "kollie Tarnue"
name = name.replace('k', 'C')
print(name)
my_color = "My favorite color is red"
my_color = my_color.replace("r", "RR")
print(my_color)

age1 = 'I am thirty-one years old'
print(age1)
age2 = age1.replace('one', 'two')
print(age2)

#cleaning the nationality and Gender column of moma datasset

unclean = 'I\'m going to the show with Peter and Eve'
clean = unclean.replace('and Eve', "")
print(clean)

nationalities = [('American'),('Spanish'), ('French')]

for n in nationalities:
    clean_open = n.replace("(", "")
    clean_both = n.replace(')', '')
    print(" ")
    print(clean_both)

print("")
print("This is the last part")
print(moma[300][2])
print(moma[400][2])
print(moma[500][2])


for row in moma:
    nationality = row[2]
    nationality = nationality.replace('(', '')
    nationality = nationality.replace(')', '')
    row[2] = nationality

    gender = row[5]
    gender = gender.replace('(','')
    gender = gender.replace(')', '')
    row[5] = gender

my_strings = 'The cool thing about this string is ' \
             'that it has a CoMbInAtIoN of UPPERCASE and lowercase' \
             'letters'
print(my_strings)

my_strings = my_strings.title()
#print(my_strings)

for row in moma:
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknow/Other"
    row[5] = gender
    #print(gender)

    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown."
    row[2] = nationality
    #print(nationality)


def clean_and_convert(date):
    if date == " ":
        date = date.replace('(', '')
        date = date.replace(')', '')
        date = int(date)
    return date


for row in moma:
    Birth_date = row[3]
    Death_date = row[4]
    Birth_date = clean_and_convert(Birth_date)
    Death_date = clean_and_convert(Death_date)
    row[3] = Birth_date
    row[4] = Death_date
    #print(Death_date)

strings = ['good!', 'morn?ing', 'good?!', 'morniZZZZng']

bad_chars = ['!',"?", "Z"]

test_data = ["1912", "1929", "1913-1923",
 "(1951)", "1994", "1934",
 "c. 1915", "1995", "c. 1912",
 "(1988)", "2002", "1957-1959",
 "c. 1955.", "c. 1970's",
 "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

# A function that strip out onwanted character from a list


def strip_c(string):
    for char in bad_chars:
        string = string.replace(char, '')
    return string


stripped_test_data = []
for str in test_data:
    str = strip_c(str)
    stripped_test_data.append(str)


def stripped(string_value):
    for char in bad_chars:
        string_value = string_value.replace(char, '')
    return string_value

print("This is the end of this project for now, but hope to continue it later on")