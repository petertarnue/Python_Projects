from csv import reader
opened = open("AppleStone - goog4_request&X-Goog-Date=20210114T104926Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=29e5b444bd18b7149d5a341fb65d8e8a02e60c4e05444601eb367fb91605626139559cae29b5293fe85bbfe5fc5e740f997775b33bd9834b9863b84.csv.", encoding= "utf-8")
readFile = reader(opened)
appData = list(readFile)

'''
freAppName = 0
for column in appData:
    name = column[1]
    price = column[5]
    if price == 0:
        freeAppName = freAppName + name
print(freAppName)

# Average rating of free apps in the "appData" data set
# Method 1.
fre_apRating = []
for elements in appData[1:]:
    rating = float(elements[7])
    price = float(elements[5])
    if price == 0.0:
        fre_apRating.append(rating)
fre_appAverRating= sum(fre_apRating)/len(appData[1:])
print(fre_appAverRating)

# Average rating of free apps in the "appData" data set
# Method 2.
fre_appRating = 0
for elements in appData[1:]:
    rating = float(elements[7])
    price = float(elements[5])
    if price == 0.0:
        fre_appRating = fre_appRating + rating
fre_avRat = fre_appRating / len(appData[1:])
print(fre_avRat)

# Average rating of non free app in "appData" data set
# Method 1.
non_fre_apRating = 0
for elements in appData[1:]:
    rating = float(elements[7])
    price = float(elements[5])
    if price != 0.0:
        non_fre_apRating = non_fre_apRating + rating
fre_appAverRating = non_fre_apRating/len(appData[1:])
print(fre_appAverRating)

# Average rating of non free app in "appData" data set
# method 2.
non_free_apps_rating = []
for element in appData[1:]:
    rating = float(element[7])
    price = float(element[5])
    if price != 0.0:
        non_free_apps_rating.append(rating)
avg_rating_non_free = sum(non_free_apps_rating)/len(appData[1:])
print(avg_rating_non_free)
'''
''''
row_1 = ["Facebook", 0.0, "USD", 2974676, 3.5]
row_2 = ["Instagram", 0.0, "USD", 2161558, 4.5]
row_3 = ["Clash of clans", 0.0, "USD", 2130804, 4.5]
row_4 = ["Temple Run", 0.0, "USD", 1724546, 4.5 ]
row_5 = ["pandora-Music & Radio", 0.0, "USD", 1126879, 4.0]


appdata = [row_1, row_2, row_3, row_4, row_5]
free_apps = []
for rows in appdata:
    name = rows[0]
    price = rows[1]

    if price == 0.0:
        free_apps.append(name)
    else:
        print("the price is greater than 0.0")

print(free_apps)
'''

''''
# calculating the average rating from colomn 7 of the
# entire data set of "appData".


#first method
rating_sum = 0
for row in appData[1:]:
    rating = float(row[7])
    rating_sum = rating_sum + rating

avg_rating = rating_sum/len(appData[1:])
print(avg_rating)
'''
''''
#second method for calculating average rating of a dataset
rating_sum = []
for elements in appData[1:]:
    rating = float(elements[7])
    rating_sum.append(rating)

avg_rating = sum(rating_sum)/len(appData[1])
print(avg_rating)
'''
'''
# Dictionaries and Frequency Table:
content_rating = ["4+", "9+", "12+", "17+"]
nums = [4433, 987, 1155, 622]

content_rating_numbers = [["4+", "9+", "12+", "17+"],[4433, 987, 1155, 622]]

content_ratings = {"4+": 4433, "9+":987, "12+":1155, "17+":622}

content_rating = {}
content_rating["4+"] = 4433
content_rating["9+"] = 987
content_rating["12+"] = 1155
content_rating["17+"] = 622
content_rating[0.2] = 'string'

over_12_n_apps = content_rating["12+"]

print(content_rating)

# Exercises for dictionaries
# 1.
print(content_ratings)
print(" newline")
d_1 = {"key_1": "first_value", 'key_2': 2, 'key_3': 3.14,
       'key_4': True, 'key_5': [4, 2, 1], 'key_6': {'inner_key': 6}}

is_in_dictionary_1 = "9+" in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if "17+" in content_ratings:
    result = "17+"
    print(result)
content_ratings["4+"] = 0
content_ratings["9+"] += 13
content_ratings["17+"] = "622"
print(content_ratings)

rating = {"4+":0, '9+':0, '12+':0, '17+':0}

for ele in rating:
    if ele in rating:
        rating[ele] += 1

print(rating)
'''
Cratings = {"4+":0, '9+':0, '12+':0, '17+':0}
rating1 = {"4+",'4+', '4+','9+', '9+', '12+', '17+'}

for x in rating1:
    if x in Cratings:
        Cratings[x] += 1
    print(Cratings)

print('final dictionary: ')
#print(Cratings)

content_ratings = {'4+':0, '9+':0, '12+':0, '17+':0}

for elements in appData[1:]:
    c_rating = elements[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
#print(content_ratings)

cont_ratings = { }
ratings = ['4+','4+', '4+', '9+', '9+','12+', '17+']
for cx in ratings:
    if cx in cont_ratings:
        cont_ratings[cx] += 1
    else:
        cont_ratings[cx] = 1
        print(cont_ratings)
print("real Final dictionary")
#print(cont_ratings)

content_ratings = {}
for row in appData[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
#print(content_ratings)

'''
content_ratings = {}
for row in appData[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
         content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
print(content_ratings)
'''
# Frequency: Proportion and percentage
# Finding the proportion and percentage of data in the data set

genre_counting = {}
for row in appData[1:]:
    genre = row[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
#print("The result is ", genre_counting)

content_ratings = {'4+': 4433, '12+': 1155, '17+': 622, '9+': 987}
total_Apps = 7197

for row in content_ratings:
    content_ratings[row] /= total_Apps
#print(content_ratings)


try:
    def opened_dataset(file_name):
        opened_file = open(file_name)
        from csv import reader
        words = reader(opened_file)
        dataApp = list(words)
        return dataApp
except:
    print("Nothing good is happening in here. "
          "please type the name of your file correctly."
          "thanks for your understanding")


pa = opened_dataset("Book2FinalDataBase.csv")
b = opened_dataset('Book3FinalDataBase.csv')
c = opened_dataset('Final Database (LUL)_Charlesville for analysis.csv')
d = opened_dataset('Final Database (LUL)_Charlesville(for analysis).csv')



try:
    def freq(file = pa, column = 11):
        pro_por = {}
        for row in file:
            cl = row[column]
            if cl in pro_por:
                pro_por[cl] += 1
            else:
                pro_por[cl] = 1
        return pro_por
except:
    print('Nothing is happened in there. Please try again.')

print(freq(column=3))
