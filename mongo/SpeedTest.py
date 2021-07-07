__author__ = 'piotr'

from pymongo import MongoClient

#ch=MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')
ch=MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')

db=ch.movieDB

#x = db.movies.find()
x = db.ratings.find()

print(type(x))

for i in x:
    print(type(i))
    print(i)
#    break

#     print(i['title'])
