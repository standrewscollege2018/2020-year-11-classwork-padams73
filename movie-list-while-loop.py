""" This program uses a while loop to repeatedly ask the user for their favourite movies. """

# set up list to store movies
movies = []

keep_asking = True

while keep_asking == True:
    movie_name = input("Enter a favourite movie: ")
    if movie_name == "stop":
        keep_asking = False
    else:
        movies.append(movie_name)
    
print(movies)

# loop through list and display the movies
for movie in movies:
    print(movie)