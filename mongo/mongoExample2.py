#! /usr/bin/python3

__author__ = 'piotr'

from pymongo import MongoClient


#cli = MongoClient()
cli=MongoClient('mongodb://student:mongoose@localhost/movieDB')
#cli=MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')

db = cli.movieDB

movies = db.movies
rating = db.ratings

score = 5
cnt = 15


# Not great; still looking at movies that scored 5 from *some* users
# But this seems to be better structured

movie_ids = rating.find({'rating' : score }).distinct('movie_id')

card = len(movie_ids)

print ('\n\t\t', cnt, 'Top-rated movies (out of', card, ')\n')

for fid in movie_ids[:cnt] : 
	for film in movies.find({'_id' : fid } ) :
		print ('\t' + film['title'])

print ('\n\n')

cli.close()
