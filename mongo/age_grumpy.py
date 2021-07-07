__author__ = 'Anastasia'

from pymongo import MongoClient

# cli = MongoClient('172.16.176.30')
# cli = MongoClient()
cli = MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')
# cli=MongoClient('mongodb://student:mongoose@172.16.176.30/movieDB')
# cli=MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')

"""
find data via cursor
"""
db = cli.movieDB

movies = db.movies
rating = db.ratings
users = db.users

score = 5

print("-----------------------------------------------------ageGroup--------------------------------------------------")

age = [45, 50]
lage = len(age)
for i in range(lage):
    age_group = age[i]
    #print(age_group)
# age_younger = 45
# age_older =50

print("-----------------------------------------------getData_of_age_rating----------------------------------------------")

# get age data
age_users = users.find({"age": age_group})
listage_users = list(age_users)

for ageinf in listage_users:
    print(ageinf)

print("------------------------------------------------rating_high_or_low------------------------------------------------")

# movie rating

getinf = rating.distinct('user_id', {'movie_id': 1193})


age_rating = rating.aggregate([{"$match":{"movie_id": 1193}},{"$group":{"_id":"movie_id", "AVGR":{"$avg":"$rating" }}}])

for h in age_rating:
    if h['AVGR'] > score and h['age'] > age_group:
        print(h)
        for film in movies.find({'_id': h['_id']}):
            print('\t' + film[u'rating'])

print ('\n\n')

cli.close()


