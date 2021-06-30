from csv import reader
handle = open('AppleStone - goog4_request&X-Goog-Date=20210114T104926Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=29e5b444bd18b7149d5a341fb65d8e8a02e60c4e05444601eb367fb91605626139559cae29b5293fe85bbfe5fc5e740f997775b33bd9834b9863b84.csv', encoding='utf-8')
readMe = reader(handle)
appData = list(readMe)

try:
    hist = {}
    for row in appData[1:]:
        rating = row[11]
        if rating in hist:
            hist[rating] += 1
        else:
            hist[rating] = 1
    #print(hist)
except:
    print('Nothing good is happening inside hear')
#print(len(hist))

# Find the Proportion of particular column in a dataset

c_ratings_proportions = {}
for value in hist:
    proportion = hist[value] / len(appData[1:])
    c_ratings_proportions[value] = proportion
#print(c_ratings_proportions)

# Find the percentage of particular column in a dataset
c_ratings_percentages = {}
for key in c_ratings_proportions:
    percentage = c_ratings_proportions[key] * 100
    c_ratings_percentages[key] = percentage

#print(c_ratings_percentages)
print('')

# Find both the proportion and the percentage of
# a particular column in one for loop.
for pt in hist:
    prop = hist[pt] / len(appData[1:])
    percent = prop * 100
    print(pt, prop)
    print(pt, percent)

data_sizes = {}
for row in appData[1:]:
    size = float(row[3])
    if size in data_sizes:
        data_sizes[size] += 1
    else:
        data_sizes[size] = 1
#print(data_sizes)
#print(len(data_sizes))

print('')
print(min(data_sizes))
print(max(data_sizes))

print(" ")

# Find the frequency of a large data set by
# using the interval method
# First Find the minimum and the maximum values in the data set
dataS = []
for row in appData[1:]:
    sizes = float(row[3])
    dataS.append(sizes)
mini_value = min(dataS)
maxi_value = max(dataS)
print(mini_value)
print(maxi_value)
'''
We want to store the frequency table as a dictionary. 
We begin by creating a dictionary with the intervals as 
dictionary keys and frequencies as dictionary values 
(we initialize all frequencies with zero):
'''
data_S = {'0 - 10 MB':0, '10 - 50 MB': 0, '50 - 100 MB': 0
          , '100 - 500 MB': 0, '500 MB +': 0}

for row in appData[1:]:
    data_ss = float(row[3])

    if data_ss <= 10000000:
        data_S['0 - 10 MB'] +=1
    elif 10000000 < data_ss <= 50000000:
        data_S['10 - 50 MB'] += 1
    elif 50000000 < data_ss <= 100000000:
        data_S['50 - 100 MB'] += 1
    elif 100000000 < data_ss <= 500000000:
        data_S['100 - 500 MB'] += 1
    elif 500000000 > data_ss:
        data_S['500 MB + '] += 1

print(data_S, data_ss)
print(" ")

rating_count_tot = []
for row in appData[1:]:
    rating_count = float(row[6])
    rating_count_tot.append(rating_count)
    min_value = min(rating_count_tot)
    max_value = max(rating_count_tot)
print(min_value)
print(max_value)

rating_freq = {'0 - 100000':0, '100000 - 500000':0, '500000 - 1000000':0
               ,'1000000 - 1500000':0, '1500000 + ': 0}
for row in appData[1:]:
    fre_rating = float(row[6])

    if fre_rating <= 100000:
        rating_freq['0 - 100000'] += 1
    elif 100000 < fre_rating <= 500000:
        rating_freq['100000 - 500000'] += 1
    elif 500000 < fre_rating <= 1000000:
        rating_freq['500000 - 1000000'] += 1
    elif 1000000 < fre_rating <= 1500000:
        rating_freq['1000000 - 1500000'] += 1
    elif 1500000 > fre_rating:
        rating_freq['1500000 + '] += 1
print('The rating frequencies are :', rating_freq)

