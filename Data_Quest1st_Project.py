'''
Opening and Exploring the Data
Openind and Reading applestore.csv file
'''''
opened = open('Applestore_final.csv', encoding='utf-8')
from csv import reader
read_f = reader(opened)
ios= list(read_f)
ios_head = ios[0]
ios = ios[1:]

# Opening and Reading googleplaystroe.csv file
opend = open('googleplaystore_final.csv', encoding='utf-8')
from csv import reader
read_file = reader(opend)
android = list(read_file)
android_head = android[0]
android = android[1:]


def explore_data(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n') # adds new (empty) line after each row
        if rows_and_columns:
            print('Number of rows:', len(dataset))
            print('Number of columns: ', len(dataset[0]))


#apple = explore_data(ios, 0, 3, True)

#google = explore_data(android, 0, 3, True)

#print(ios_head)
print('\n')
#explore_data(appledata_set, 0, 3, True)


#print('The incorrect row is :',android[10472]) # Incorrect row
print('\n')
#print(android_head) # header
print('\n')
#print(android[0])
print('\n')

'''
The row 10472 corresponds to the app Life Made WI-Fi Touchscreen Photo Frame, and we can see 
that the rating is 19. This is clearly off because the maximum rating for a Google Play app is 5 (as 
mentioned in the discussions section, this problem is caused by a missing value in the 'Category'
column). As a consequence, we'll delete this row.
'''
#print(len(android))
del android[10472]
print(len(android))
#print(len(android))

# Removing Duplicate Entries

for app in android:
    name = app[0]
    if name == 'Instagram':
        print(app)

# finding duplicate apps

duplicate_apps = []
unique_apps = []
for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)

print('\n')
print('Number of duplicate apps: ',len(duplicate_apps))
print('\n')
print('Example of dublicate apps are: ', duplicate_apps[:15])
print('Number of unique apps is: ', len(unique_apps))

'''
Above, I Created two lists: one for storing the name of duplicate apps, and one for 
storing the name of unique apps.
 Looped through the android data set (the Google Play data set), and for each 
iteration:
o We saved the app name to a variable named name.
o If name was already in the unique_apps list, we appended name to 
the duplicate_apps list.
o Else (if name wasn't already in the unique_apps list), we appended name to 
the unique_apps list.
'''

'''
In Addition,
We don't want to count certain apps more than once when we analyze data, 
so we need to remove the duplicate entries and keep only one entry per app. 
One thing we could do is remove the duplicate rows randomly, but we could 
probably find a better way.
If you examine the rows we printed for the Instagram app, the main difference 
happens on the fourth position of each row, which corresponds to the number 
of reviews. The different numbers show the data was collected at different 
times.
We don't want to count certain apps more than once when we analyze data, 
so we need to remove the duplicate entries and keep only one entry per app. 
One thing we could do is remove the duplicate rows randomly, but we could 
probably find a better way.

If you examine the rows we printed for the Instagram app, the main difference 
happens on the fourth position of each row, which corresponds to the number of reviews.The different numbers 
show that the data was collected at different times. We can use this to build a criterion for keeping 
rows. We won't remove rows randomly, but rather we'll keep the rows that have the highest number 
of reviews because the higher the number of reviews, the more reliable the ratings.

To do this, we will:
● Create a dictionary where each key is a unique app name, and the value is the 
   highest number of reviews of that app
● Use the dictionary to create a new data set, which will have only one entry per app 
(and we only select the apps with the highest number of reviews)
'''

reviews_max = {}
for app in android:
    name = app[0]
    n_reviews = float(app[3])
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

print('\n')
#print('the review max is:',reviews_max)

print('Expected lenght:', len(android) - 1181)
print('Action length:', len(reviews_max))

android_clean = []
already_added = []
for apps in android:
    names = apps[0]
    n_review = float(apps[3])
    if (reviews_max[names] == n_review) and (names not in already_added):
        android_clean.append(apps)
        already_added.append(names)

explore_data(android_clean, 0, 3, True)

# Removing Non-English Apps
'''
print(ios[813[1]])
print(ios[6731][1])

print(android_clean[4412][0])
print(android_clean[7940][0])
'''

def is_english(string):
    for character in string:
        if ord(character) > 127:
           return False

    return True

print(is_english('Instagram'))

'''
The function seems to work fine, but some English app names use emojis or other symbols (™, —
(em dash), – (en dash), etc.) that fall outside of the ASCII range. Because of this, we'll remove useful 
apps if we use the function in its current form.
'''

def is_english(string):
    non_ascii = 0
    for character in string:
        if ord(character) > 127:
            non_ascii += 1
    if non_ascii > 3:
        return False
    else:
        return True


print(is_english('Docs To Go™ Free Office Suite'))

android_english = []
ios_english = []
for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)


for app in ios:
    name = app[1]
    if is_english(name):
        ios_english.append(app)


print("Below is android English")
#explore_data(android_english, 0, 3, True)
print('\n')
#explore_data(ios_english, 0, 3, True)

# Isolating the Free Apps
'''
As we mentioned in the introduction, we only build apps that are free to download and install, and our 
main source of revenue consists of in-app ads. Our data sets contain both free and non-free apps, 
and we'll need to isolate only the free apps for our analysis. Below, we isolate the free apps for both 
our data sets.
'''
android_final = []
ios_final = []

for app in android_english:
    price = app[7]
    if price == '0':
        android_final.append(app)

for appp in ios_english:
    price = appp[4]
    if price == '0.0':
        ios_final.append(appp)


print(len(android_final))
print(len(ios_final))

# We have completed the below five listed task so far
'''
we have spent a good amount of time on cleaning data, and:
Removed inaccurate data
 Removed duplicate app entries
 Removed non-English apps
 Isolated the free apps
'''
# Data Analysis
'''
As we mentioned in the introduction, our aim is to determine the kinds of apps 
that are likely to attract more users because our revenue is highly influenced 
by the number of people using our apps.
To minimize risks and overhead, our validation strategy for an app idea is 
comprised of three steps:
1. Build a minimal Android version of the app, and add it to Google Play.
2. If the app has a good response from users, we develop it further.
3. If the app is profitable after six months, we build an iOS version of the app and 
add it to the App Store.

Because our end goal is to add the app on both the App Store and Google Play, we need to find app 
profiles that are successful on both markets. For instance, a profile that might work well for both 
markets might be a productivity app that makes use of gamification.
Let's begin the analysis by getting a sense of the most common genres for each market. For this, we'll 
build a frequency table for the prime_genre column of the App Store data set, and the Genres and 
Category columns of the Google Play data set.

'''
# Most common apps by Genre

def freq_table(dataset, index):
    table = {}
    total = 0
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1

    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage

    return table_percentages


def display_table(datasets, indexes):
    table = freq_table(datasets, indexes)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1],'.',entry[0])


display_table(ios_final, -5) # output the Genre analysis on ios store
print('')
'''
We can see that among the free English apps, more than a half (58.16%) are games. Entertainment 
apps are close to 8%, followed by photo and video apps, which are close to 5%. Only 3.66% of the 
apps are designed for education, followed by social networking apps which amount for 3.29% of the 
apps in our data set.
The general impression is that App Store (at least the part containing free English apps) is dominated 
by apps that are designed for fun (games, entertainment, photo and video, social networking, sports, 
music, etc.), while apps with practical purposes (education, shopping, utilities, productivity, lifestyle, 
etc.) are more rare. However, the fact that fun apps are the most numerous doesn't also imply that 
they also have the greatest number of users — the demand might not be the same as the offer.
Let's continue by examining the Genres and Category columns of the Google Play data set (two 
columns which seem to be related).
'''

display_table(android_final, 1) # output the Genre analysis on google play store
display_table(android_final, -4)
'''
he landscape seems significantly different on Google Play: there are not that many apps designed 
for fun, and it seems that a good number of apps are designed for practical purposes (family, tools, 
business, lifestyle, productivity, etc.). However, if we investigate this further, we can see that the family 
category (which accounts for almost 19% of the apps) means mostly games for kids.
Even so, practical apps seem to have a better representation on Google Play compared to App Store. 
This picture is also confirmed by the frequency table we see for the Genres column:'''

# Most Popular Apps by Genre on the Apple Store
'''
One way to find out what genres are the most popular (have the most users) is to calculate the average 
number of installs for each app genre. For the Google Play data set, we can find this information in 
the Installs column, but for the App Store data set this information is missing. As a workaround, we'll 
take the total number of user ratings as a proxy, which we can find in the rating_count_tot app.
Below, we calculate the average number of user ratings per app genre on the App Store:
'''
genres_ios = freq_table(ios_final, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1

    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)


for app in ios_final:
    if app[-5] == 'Navigation':
        print(app[1], '.', app[5])  # print name and number of rating
print('')
for app in ios_final:
    if app[-5] == 'Reference':
        print(app[1], ":", app[5])

display_table(android_final, 5)

categories_android = freq_table(android_final, 1)
for category in categories_android:
    totals = 0
    len_category = 0
    for app in android_final:
        category_app = app[1]
        if category_app == category:
            n_installs = app[5]
            n_installs = n_installs.replace(',','')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    print(category,':', avg_n_installs)


for ap in android_final:
    if ap[0] == 'COMMUNICATION' and (ap[5] == '1,000000000+' or ap[5] == '500,000,000+' or ap[5] == '100,000,000+'):
        print(ap[0], ':', ap[5])
