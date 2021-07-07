#! /usr/bin/python3
__author__ = 'piotr'


from pymongo import MongoClient


# cli = MongoClient()
# cli=MongoClient('mongodb://student:mongoose@localhost/movieDB')
# cli=MongoClient('mongodb://student:mongoose@172.16.176.30/movieDB')

cli=MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')


db = cli.movieDB

# movies = db.movies
# rating = db.ratings

colls = [ 'movies', 'ratings' ]
movies = eval('db.'+colls[0]);
rating = eval('db.'+colls[1]);


score = 4.4
noRevs = 100


# Coming close to the goal, but no cigar yet:
# looking for movies with high avg score, based on a sensible number of reviews


avgs = rating.aggregate( [ {'$group' : { '_id' : '$movie_id', 'AVG': {'$avg' : '$rating' }, 'CNT': {'$sum' : 1} } } ] )


print ('\n\t\tTop-rated movies' )
print ('\t (average score above', score, 'out of 5, based on at least', noRevs, 'reviews) \n')

for y in avgs :
	if y['AVG'] > score and y['CNT'] >= noRevs :
		for film in movies.find({'_id' : y['_id'] } ) :
			print ('\t' + film[u'title'])

print ('\n\n')
