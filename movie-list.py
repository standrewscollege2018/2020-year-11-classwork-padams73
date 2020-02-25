""" This programs asks the user to enter 3 movies, then stores them in a list, finally printing them out. """

# set up an empty list to store the movies
movies = []

# start loop to ask for three movies
for i in range (0,3):
    movie_name = input("Name a favourite movie: ")
    movies.append(movie_name)

print(movies)