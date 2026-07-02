"""
generate_data.py
Generates a synthetic movie ratings dataset and saves it to data/movies.csv.
"""

import os
import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

NUM_MOVIES = 500

GENRES = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Animation"]

# Genre biases: some genres tend to score higher
GENRE_BIAS = {
    "Action": 0.0,
    "Comedy": 0.1,
    "Drama": 0.3,
    "Horror": -0.2,
    "Romance": 0.0,
    "Sci-Fi": 0.2,
    "Thriller": 0.1,
    "Animation": 0.4,
}

def generate_movies(n=NUM_MOVIES):
    genres = np.random.choice(GENRES, size=n)
    years = np.random.randint(1990, 2024, size=n)

    # Base rating centered around 6.0 with some noise
    base_ratings = np.random.normal(loc=6.0, scale=1.2, size=n)

    # Apply genre bias
    biases = np.array([GENRE_BIAS[g] for g in genres])

    # Slight upward trend over years (newer movies rated slightly higher on average)
    year_effect = (years - 1990) * 0.01

    ratings = base_ratings + biases + year_effect

    # Clamp ratings to [1.0, 10.0]
    ratings = np.clip(ratings, 1.0, 10.0).round(1)

    # Number of votes: log-normal distribution
    votes = np.random.lognormal(mean=7.0, sigma=1.2, size=n).astype(int)
    votes = np.clip(votes, 50, 500000)

    titles = [f"Movie_{i+1:04d}" for i in range(n)]

    df = pd.DataFrame({
        "title": titles,
        "genre": genres,
        "year": years,
        "rating": ratings,
        "votes": votes,
    })

    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = generate_movies()
    output_path = os.path.join("data", "movies.csv")
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")
    print(f"Shape: {df.shape}")
    print(df.head())