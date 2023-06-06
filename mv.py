# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie dataset
movies = pd.read_csv("movies.csv")

# Calculate the cosine similarity between all movie pairs
similarity = cosine_similarity(movies.iloc[:,1:])

# Write a function to get recommendations for a given movie
def recommend_movies(title, similarity=similarity):
    # Get the index of the movie
    index = movies[movies.title == title].index[0]
    
    # Get the pairwise similarity scores of all movies with that movie
    scores = list(enumerate(similarity[index]))
    
    # Sort the movies based on the similarity scores
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the top 5 most similar movies (excluding the movie itself)
    scores = scores[1:6]
    
    # Return the titles of the most similar movies
    movie_indices = [i[0] for i in scores]
    return movies['title'].iloc[movie_indices]

# Test the recommendation function with a sample movie
print(recommend_movies("The Matrix"))