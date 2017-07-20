# import repo

class MovieCollectionController(object):

	def __init__(self, repo):
		self.repo = repo

	def iJustWatchedANewMovie(title: string, year: int, director: string) -> None:
		movie = Movie(title, year, director)
		self.repo.saveMovie(movie)
		# print message

	def exportAllTheMoviesToCsv() -> None:
		movies = self.repo.findAll()
		# convert list to csv
		# output the file
		# bonus: upload the file

	def exportAllTheMoviesToJson() -> None:
		movies = self.repo.findAll()
		# convert list to json
		# output the file
		# bonus: upload the file

	def howManyFreakinMoviesInThere() -> None:
		all_the_movies = self.repo.findAll()
		return len(all_the_movies)




