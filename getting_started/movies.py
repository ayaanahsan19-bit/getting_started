import pandas as pd
import matplotlib.pyplot as plt

sample_data = {
    'show_id': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8'],
    'type': ['Movie', 'Movie', 'Movie', 'TV Show', 'Movie', 'Movie', 'Movie', 'Movie'],
    'title': ['Action Movie 1', 'Comedy Movie', 'Action Movie 2', 'TV Series', 'Drama Movie', 'Action Movie 3', 'Thriller', 'Romance'],
    'director': ['Director A', 'Director B', 'Director C', 'Director D', 'Director E', 'Director F', 'Director G', 'Director H'],
    'genre': ['Action', 'Comedy', 'Action', 'Drama', 'Drama', 'Action', 'Thriller', 'Romance'],
    'release_year': [1995, 1998, 1992, 1999, 2001, 1994, 1997, 1996],
    'duration': [120, 95, 85, 45, 110, 88, 105, 92]
}

netflix_df = pd.DataFrame(sample_data)

netflix_df.to_csv("netflix_data.csv", index=False)

print("Sample netflix_data.csv created!")

netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]
movies_1990s = subset[(subset["release_year"] < 2000)]

print(f"Found {len(movies_1990s)} movies from 1990s")

plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]
short_movie_count = 0

for label, row in action_movies_1990s.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1

print(f"Number of short action movies (<90 min): {short_movie_count}")