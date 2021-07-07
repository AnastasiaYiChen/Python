#! /usr/bin/python3

__author__ = 'piotr'

from pymongo import MongoClient

"""
Computing average rating of a movie entitled "Grand Canyon (1991)"
( do-it-yourself way ;)
"""

#cli = MongoClient()
cli=MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')

db = cli.movieDB
movies = db.movies
rating = db.ratings

movie_title="Grand Canyon (1991)"
#movie_title="GoldenEye (1995)"

ids= [ n["_id"] for n in movies.find({"title": movie_title}, {"_id": 1}) ]
print(ids)
print(ids[0])

val=[x["rating"] for x in rating.find({"movie_id": ids[0]}) ]
print(val)


sum=sum(val)
cnt=len(val)


print("Movie:", movie_title, "\nAverage rating:", sum/cnt, "(based on", cnt, "ratings).")

