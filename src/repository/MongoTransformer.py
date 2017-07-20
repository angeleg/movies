from Movie import Movie

class MongoTransformer(object):

	def toDict(movie: Movie) -> dict:
		res = {}
		res['title'] = movie.title
		res['year'] = movie.year
		res['director'] = movie.director
		return res


	def toEntity(list: dict) -> Movie:
		return Movie(
			list['title'],
			list['year'],
			list['director']
		)


