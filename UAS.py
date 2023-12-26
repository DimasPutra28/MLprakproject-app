import pandas as pd
import random

# Read the dataset
data = pd.read_csv("piki_dataset.csv")

# Get user input for user_id and song_id
user_id = input("Enter user ID: ")
song_id = input("Enter song ID: ")

# Filter the data based on user_id and song_id
song_data = data[(data['user_id'] == int(user_id)) & (data['song_id'] == int(song_id))]

if song_data.empty:
    print(f"Data not found for user {user_id} and song {song_id}.")
else:
    liked_value = song_data['liked'].values[0]

    if liked_value == 1:
        # Get top 10 recommended songs with higher spotify_popularity, where liked=1
        liked_songs = data[(data['liked'] == 1) & (data['song_id'] != int(song_id))]
        recommendations = liked_songs.nlargest(10, 'spotify_popularity')[['song_id', 'spotify_popularity']]
        print(f"Top 10 recommended songs for user {user_id} with liked=1")
        print(recommendations)
    else:
        # Get top 10 recommended songs with higher spotify_popularity randomly, where liked=0
        all_songs = data[data['song_id'] != int(song_id)]
        random_recommendations = all_songs.sample(10)[['song_id', 'spotify_popularity']]
        print(f"Top 10 random recommendations for user {user_id} with liked=0")
        print(random_recommendations)