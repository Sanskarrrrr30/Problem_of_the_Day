# Movie Rating Aggregator

# Function to group ratings by movie
# Output: {'MovieName': [ratings]}
def group_ratings_by_movie(reviews):
    movie_groups = {}
    for review in reviews:
        movie = review["movie"]        # extract movie name
        rating = review["rating"]      # extract rating
        # add rating to the list of that movie
        movie_groups.setdefault(movie, []).append(rating)
    return movie_groups

# Function to compute average rating for each movie
# Output: {'MovieName': average_rating}
def compute_average_ratings(movie_groups):
    # average = sum of ratings / number of ratings
    return {movie: sum(ratings) / len(ratings) for movie, ratings in movie_groups.items()}

# Function to find movie with highest average rating
def find_top_movie(avg_ratings):
    # max returns key with highest value using avg_ratings.get
    return max(avg_ratings, key=avg_ratings.get)


# Function to filter movies with rating >= threshold (default 8.5)
def get_must_watch_movies(avg_ratings, threshold=8.5):
    # list comprehension to filter movies
    return [movie for movie, avg in avg_ratings.items() if avg >= threshold]


# Function to find each user's favorite movie (highest rated)
def find_user_favorites(reviews):
    user_best = {}
    for review in reviews:
        user = review["user"]      # extract user
        movie = review["movie"]    # extract movie
        rating = review["rating"]  # extract rating

        # update if:
        # 1. user not seen before OR
        # 2. current rating is higher than stored rating
        if user not in user_best or rating > user_best[user][1]:
            user_best[user] = (movie, rating)

    # convert {user: (movie, rating)} → {user: movie}
    return {user: movie for user, (movie, _) in user_best.items()}

# Main driver function
def main():
    try:
        # Input data (list of dictionaries)
        reviews = [
            {"movie": "Inception", "user": "alice", "rating": 9},
            {"movie": "Dune", "user": "bob", "rating": 8},
            {"movie": "Inception", "user": "bob", "rating": 7},
            {"movie": "Interstellar", "user": "alice", "rating": 10},
            {"movie": "Dune", "user": "charlie", "rating": 9},
            {"movie": "Interstellar", "user": "charlie", "rating": 8},
        ]

        # Step 1: Group ratings by movie
        movie_groups = group_ratings_by_movie(reviews)

        # Step 2: Compute average ratings
        avg_ratings = compute_average_ratings(movie_groups)

        # Step 3: Find highest-rated movie
        top_movie = find_top_movie(avg_ratings)

        # Step 4: Get must-watch movies (avg >= 8.5)
        must_watch = get_must_watch_movies(avg_ratings)

        # Step 5: Get each user's favorite movie
        user_favs = find_user_favorites(reviews)

        # Display results
        print("avg_ratings =", avg_ratings)
        print("top_movie =", top_movie)
        print("must_watch =", must_watch)
        print("user_favs =", user_favs)

    except Exception as e:
        # Handle unexpected errors
        print("Error:", e)


# Entry point of program
if __name__ == "__main__":
    main()