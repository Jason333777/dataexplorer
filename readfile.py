import csv 

with open('action.csv', 'r') as file:
    reader= csv.reader(file)


def load_movies(filename):
    with open(filename, 'r') as file:
        movies = file.readlines()
    return [movie.strip() for movie in movies]

