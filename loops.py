movies = ['Spiderman', 'Iron Man', 'Godzilla x Kong', 'Minions']
ratings = [7.3, 7.9, 6.1, 6.4]
genres = ['comedy', 'action', 'action', 'comedy']

for movie in movies: 
    print(movie)

total_ratings = 0 
for rating in ratings:
    total_ratings += rating
    print('Total Rating:', total_ratings)

for i in range(len(movies)):
    print(movies[i], 'has a rating of', ratings[i]) 

highest_rating = max(ratings)
index = ratings.index(highest_rating)
print('The highest-rated movie is:', movies[index])

filtered_movies = []
for i in range(len(movies)):
    if genres[i] == 'action':
        filtered_movies.append(movies[i])
print('Action movies:', filtered_movies)