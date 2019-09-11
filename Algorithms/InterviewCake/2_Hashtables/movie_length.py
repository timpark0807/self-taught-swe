def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_dict = {}

    for index, movie_length in enumerate(movie_lengths):
        movie_dict[movie_length] = index

    for movie_length in movie_lengths:
        needed = flight_length - movie_length
        if needed in movie_dict:
            return True
        
    return False
        


result = can_two_movies_fill_flight([1, 2, 3, 9, 0,86], 7)
