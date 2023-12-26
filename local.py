from flask import Flask, render_template, request,session
import csv
import pandas as pd
import random


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkeydimas"

# Load dataset
data = pd.read_csv("piki_dataset.csv")

@app.route('/')
def index():
    return render_template('layout.html')  # Render your HTML form here

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    user_id = request.form['user_id']
    song_id = request.form['song_id']

    song_data = data[(data['user_id'] == int(user_id)) & (data['song_id'] == int(song_id))]

    if song_data.empty:
        return f"Data not found for user {user_id} and song {song_id}."
    else:
        liked_value = song_data['liked'].values[0]

        if liked_value == 1:
            liked_songs = data[(data['liked'] == 1) & (data['song_id'] != int(song_id))]
            recommendations = liked_songs.nlargest(10, 'spotify_popularity')[['id','song_id','liked', 'spotify_popularity']]
            return render_template('main.html', user_id=user_id, liked=1, recommendations=recommendations)
        else:
            all_songs = data[data['song_id'] != int(song_id)]
            random_recommendations = all_songs.sample(10)[['id','song_id','liked', 'spotify_popularity']]
            return render_template('main.html', user_id=user_id, liked=0, recommendations=random_recommendations)

if __name__ == '__main__':
    app.run(debug=True)