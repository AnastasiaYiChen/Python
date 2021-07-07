#! /usr/bin/env python3

__author__ = 'piotr'

from pymongo import MongoClient


#cli = MongoClient('172.16.176.30')
#cli = MongoClient()
cli=MongoClient('mongodb://student:mongoose@localhost/movieDB')
#cli=MongoClient('mongodb://student:mongoose@172.16.176.30/movieDB')
#cli=MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')

db = cli.movieDB

movies = db.movies
rating = db.ratings

score = 4.7


# A bit different take (but is it better?):
# looking for movies with high avg score

print ('\n\t\tTop-rated movies (average score above ', score, ' out of 5)\n')

avgs = rating.aggregate( [{'$group' : { '_id' : '$movie_id', 'AVG': {'$avg' : '$rating' }}}] )

for y in avgs :
	if y['AVG'] > score :
		for film in movies.find({'_id' : y['_id'] } ) :
			print ('\t' + film['title'])

print ('\n\n')

cli.close()
