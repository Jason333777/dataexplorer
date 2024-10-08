movies = ['Spiderman', 'Iron Man', 'Godzilla x Kong', 'Minions']
ratings = [7.3, 7.9, 6.1, 6.4]
genres = ['comedy', 'action', 'action', 'comedy']

#function to calculate the average rating
def calculate_average_rating(ratings):
    total = sum(ratings)
    return total/len(ratings)

#print out average rating
average = calculate_average_rating(ratings)
print('Average Rating:', average)

#finding the highest-rated movie from the list
def find_highest_rated(movies, ratings):
    highest_rating = max(ratings)
    index = ratings.index(highest_rating)
    return movies [index]

top_movie= find_highest_rated(movies, ratings)
print('Top rated movie:', top_movie)


def filtered_by_genre():
    filtered_movie = []
    for i in range(len(movies)):
        if genres[i] == 'action':
            filtered_movie.append(movies[i])
    print('Action movies', filtered_movie)

filtered_by_genre()