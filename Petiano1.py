from csv import reader

Op = open('AppleStone - goog4_request&X-Goog-Date=20210114T104926Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=29e5b444bd18b7149d5a341fb65d8e8a02e60c4e05444601eb367fb91605626139559cae29b5293fe85bbfe5fc5e740f997775b33bd9834b9863b84.csv', encoding= 'utf-8')
rD = reader(Op)
appDataSet = list(rD)

# Find the histogram or frequency of particular column
# in the dataset (appDataSet)

''''
free_APP_rating = []
for value in appDataSet[1:]:
    rating = float(value[7])
    price = float(value[5])
    if price == 0.0:
        free_APP_rating.append(rating)
avg = sum(free_APP_rating) / len(free_APP_rating)
print(avg)

print("")
non_freeApp_rating = []
for va in appDataSet[1:]:
    rating = float(va[7])
    price = float(va[5])
    if price != 0.0:
        non_freeApp_rating.append(rating)
avg1 = sum(non_freeApp_rating)/len(non_freeApp_rating)
print(avg1)
print('')
content_rating = {'4+':0,'9+':0,'12+':0,'17+':0}
numbers = ['4+','4+','4+','9+','9+','12+','17+']
for x in numbers:
    if x in content_rating:
        content_rating[x] += 1
    print(content_rating)
#print("Final dictionary")

cont_Rating = {'4+':0,'9+':0,'12+':0,'17+':0}
for row in appDataSet[1:]:
    c_rating = row[10]
    if c_rating in cont_Rating:
        cont_Rating[c_rating] += 1
print(cont_Rating)
'''
cont_Rating = {}
for row in appDataSet[1:]:
    c_rating = row[10]
    if c_rating not in cont_Rating:
        cont_Rating[c_rating] = 1
    else:
        cont_Rating[c_rating] +=1
print(cont_Rating)

print('')
C_Rating = {}
for row in appDataSet[1:]:
    CR = row[10]
    if CR in C_Rating:
        C_Rating[CR] += 1
    else:
        C_Rating[CR] = 1
print(C_Rating)

contentRatingNumber = [['4+','9+','12+','17+'],[4433,987,1155,622]]

ratings = ['4+','4+','4+','9+','9+','12+','17+']
print('')
cont_ratings = {}
for row in appDataSet[1:]:
    C_rating = row[11]
    if C_rating in cont_ratings:
        cont_ratings[C_rating] += 1
    else:
        cont_ratings[C_rating] = 1
print(cont_ratings)

for ev in cont_ratings:
    proportion = cont_ratings[ev] / len(cont_ratings)
print('content_rating proportion:',proportion)

# proportion of each of the (content rating) in the data set

genre_counting = {}
for row in appDataSet[1:]:
    genre = row[12]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
print(genre_counting)
print('')

EveD = {}
for row in appDataSet[1:]:
    lineRow = row[12]
    EveD[lineRow] = EveD.get(lineRow,0) + 1
print(EveD)

print('')

#Finding the Proportion of each content rating column in the dataset
for value in EveD:
    EveD[value] /= len(EveD)
print('The proportions are: ', EveD)
print(" ")
# Finding the percentage of each content rating colomn in the dat
for lp in cont_ratings:
    cont_ratings[lp] /= len(cont_ratings)
    cont_ratings[lp] /= 100
print('this is te percentage:',cont_ratings)
