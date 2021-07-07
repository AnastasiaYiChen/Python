
__author__ = 'piotr'

import pymongo

# Authorized access required!
# cli=pymongo.MongoClient('mongodb://student:mongoose@localhost/movieDB')
cli=pymongo.MongoClient('mongodb://student:mongoose@172.16.176.24/movieDB')

db = cli.movieDB

movies = db.movies
rating = db.ratings

score = 5

# Another try to find "the best" movie...
# Now looking for movies that scored 5 from *EVERY* users that rated them.

# Note that what follows is the standard way of answering those hard "EVERY" questions.
# (Try to solve the same problem using a relational version of the database. See? )

# These 2 lines work here, but not in the current mongo shell:
# movie_ids = rating.find({'rating' : score }).distinct('movie_id')
# leser_movie_ids = rating.find({'rating' : {'$lt' : 5} }).distinct('movie_id')
# A better (new) way (that works in the shell as well):

movie_ids = rating.distinct('movie_id', {'rating' : score })
leser_movie_ids = rating.distinct('movie_id',{'rating' : {'$lt' : 5}} )


for x in leser_movie_ids : 
	try :
		movie_ids.remove(x)
	except ValueError :
		continue		


card = len(movie_ids)

print ('\n\t\tTop-rated movies (5 from every user) ')

for fid in movie_ids :
	for film in movies.find({'_id' : fid } ) :
		print ('\t' + film[u'title'])

print ('\n\n')

cli.close()
# Challenge: modify the above to show how many users rated each of those titles...