"""Solutions for the movie dictionary tasks."""

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]


def is_high_score(movie):
    """Return True if one movie has an IMDB score above 5.5."""
    return movie["imdb"] > 5.5


def high_score_movies(movie_list):
    """Return movies with an IMDB score above 5.5."""
    return [movie for movie in movie_list if is_high_score(movie)]


def movies_by_category(movie_list, category):
    """Return movies from one category, ignoring letter case."""
    return [movie for movie in movie_list if movie["category"].lower() == category.lower()]


def average_score(movie_list):
    """Return the average IMDB score, or 0 for an empty list."""
    if not movie_list:
        return 0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)


def category_average(movie_list, category):
    """Return the average IMDB score for one category."""
    return average_score(movies_by_category(movie_list, category))


if __name__ == "__main__":
    # Here is a short test of the movie solutions.
    print(is_high_score(movies[0]))
    print([movie["name"] for movie in high_score_movies(movies)])
    print([movie["name"] for movie in movies_by_category(movies, "Romance")])
    print(average_score(movies))
    print(category_average(movies, "Romance"))
