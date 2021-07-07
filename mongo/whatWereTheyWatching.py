__author__ = 'Anastasia'

from pymongo import MongoClient

cli = MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')

db = cli.movieDB
movies = db.movies
rating = db.ratings
cnt = 20

# User input
u_input = input("Please input a number:")

num = int(u_input)

# Getting data from Mongodb
get_user = rating.distinct('movie_id', {'user_id': num })

print('\n\t\t', cnt, 'Top-rated movies (out of ', len(get_user), ')\n')

# print title that rated
for val in get_user:
    if cnt:
        for film in movies.find({'_id': val}):
            print('\t' + film['title'])
            cnt = cnt - 1
    else:
        break

print('\n\n')

cli.close()
