# Function to calculate similarity between users using cosine similarity
def cosine_similarity(user1, user2):
    dot_product = 0
    norm_user1 = 0
    norm_user2 = 0

    for rating1, rating2 in zip(user1, user2):
        dot_product += rating1 * rating2
        norm_user1 += rating1 ** 2
        norm_user2 += rating2 ** 2

    if norm_user1 == 0 or norm_user2 == 0:
        return 0

    return dot_product / ((norm_user1 ** 0.5) * (norm_user2 ** 0.5))

# Function to recommend movies to a user based on collaborative filtering
def recommend_movies(user_id, movie_ratings, movie_names):
    similar_users = []
    target_user_ratings = movie_ratings[user_id]

    for idx, user_ratings in enumerate(movie_ratings):
        if idx != user_id:
            similarity = cosine_similarity(target_user_ratings, user_ratings)
            similar_users.append((idx, similarity))

    similar_users.sort(key=lambda x: x[1], reverse=True)

    recommendations = []
    for movie_idx, rating in enumerate(target_user_ratings):
        if rating == 0:
            predicted_rating = 0
            sim_sum = 0
            for user_idx, similarity in similar_users:
                if movie_ratings[user_idx][movie_idx] != 0:
                    predicted_rating += similarity * movie_ratings[user_idx][movie_idx]
                    sim_sum += similarity
            if sim_sum != 0:
                predicted_rating /= sim_sum
                recommendations.append((movie_idx, predicted_rating))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [(movie_names[movie_idx], predicted_rating) for movie_idx, predicted_rating in recommendations]

# Test the movie recommendation system
def main():
    # Sample user-item matrix (ratings) for movies
    movie_ratings = [
        [5, 4, 0, 0, 3],  # User 1
        [0, 5, 4, 0, 4],  # User 2
        [4, 0, 5, 3, 0],  # User 3
        [0, 4, 0, 5, 4],  # User 4
        [3, 0, 4, 0, 5]   # User 5
    ]

    # List of movie names
    movie_names = [
        "A SILENT VOICE",
        "YOUR NAME",
        "WEATHERING WITH YOU",
        "SUZUME",
        "A WHISKER AWAY"
    ]

    user_id = int(input("Enter the user ID (0-4): "))  # assuming user IDs are from 0 to 4
    recommended_movies = recommend_movies(user_id, movie_ratings, movie_names)

    print("Recommended movies for user", user_id)
    for movie_name, predicted_rating in recommended_movies:
        print("Movie:", movie_name, "Predicted Rating:", round(predicted_rating, 2))

if __name__ == "__main__":
    main()
