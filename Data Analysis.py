
from csv import reader
opened = open('artworks_final.csv', encoding='utf-8')
read_file = reader(opened)
moma = list(read_file)
moma = moma[1:]
print('\n')

# Cleaning unwanted characters from the  nationality and gender
# column of moma dataset.
nationality_f = []
gender_f = []
for row in moma:
    nationality = row[2]
    nationality = nationality.replace('(','')
    nationality = nationality.replace(')', '')
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality
    nationality_f.append(nationality)

    gender = row[5]
    gender = gender.replace('(','')
    gender = gender.replace(')', '')
    gender = gender.title()
    if not gender:
        gender = " Gender unknown/Other"
    row[5] = gender
    gender_f.append(gender)

'''
Data analysis question to answer:
1. Calculate how old the artist was when they created their work.
2.analyze and interpret the distribution of artist ages.
3.Create functions which summarize our data.
4.Print summaries in an easy-to-read-way.
'''

unwanted_symbol = ['(',')','c.','','s']


def strip(string):
    for value in unwanted_symbol:
        string = string.replace(value, '')
    return string

# 1. Calculating   how old the artist was when they created their work.
ages = []
for row in moma:
    c3 = row[3]
    c4 = row[4]
    c6 = row[6]
    birth_date = strip(c3)
    death_date = strip(c4)
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date
    c_6 = strip(c6)
    if "-" in c_6:
        date = c_6.split("-")
        date_one = date[0]
        date_two = date[1]
        date_one = int(date_one)
        date_two = int(date_two)
        date = (date_one + date_two) / 2
        date = round(date)
        if type(birth_date) == int:
            age = date - birth_date
        else:
            age = 0
        ages.append(age)

final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)

print(final_ages)


# Finding the frequencies of the nationality and
# gender column of the moma dataset.

gender_freq = {}
for gd in gender_f[1:]:
    if gd not in gender_freq:
        gender_freq[gd] = 1
    else:
        gender_freq[gd] += 1

nationality_freq = {}
for nt in nationality_f[1:]:
    if nt not in nationality_freq:
        nationality_freq[nt] = 1
    else:
        nationality_freq[nt] += 1

# Analysis of nationality column of moma dataset.
# First method
for nat, num in nationality_freq.items():
    ex1 = "There are {num:,} {nat} pepple who contributed to the artworks of moma dataset."
    output = ex1.format(num = num, nat = nat)

# second method
ex = "The population of {c} is {s:,.2f} millions "
for nat, size in nationality_freq.items():
    out = ex.format(c=nat,s=size)
    #print(out)

for gender, gen_size in gender_freq.items():
    example = "There are {size:,} {gen} who contributed to this beautiful work"
    out = example.format(size = gen_size, gen = gender)

exa = "The number of {f} who are actively working is {n:,}"
for gen, g_size in gender_freq.items():
    out = exa.format(f=gen, n=g_size)
    #print(out)

# Analysis of Artist column in the moma dataset.

artist_freq = {}
for row in moma[1:]:
    artist = row[1]
    if artist in artist_freq:
        artist_freq[artist] += 1
    else:
        artist_freq[artist] = 1

text = "{at_name} has contributed {nu} number artwork to this company."
for art, num in artist_freq.items():
    output = text.format(at_name = art, nu=num)
    #print(output)


def art_summary(artist):
    num_artwork = artist_freq[artist]
    templete_string = "There are {num} artwork done by {name} in the moma dataset"
    output = templete_string.format(num=num, name= artist)
    print(output)















