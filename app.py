import os
import spotipy
from flask import Flask, request, render_template
from io import BytesIO
import base64
from spotipy.oauth2 import SpotifyClientCredentials
from plot_utils import plot_genre_distribution

app = Flask(__name__)

# get spotify credentials from environment
spotify_id = os.getenv("SPOTIPY_CLIENT_ID")
spotify_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not spotify_id or not spotify_secret:
    raise ValueError("spotify credentials not found in environment")

# initialize spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_id, client_secret=spotify_secret))

# route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# route to fetch and display playlist data
@app.route('/playlist', methods=['POST'])
def playlist():
    playlist_id = request.form['playlist_id']
    try:
        results = sp.user_playlist_tracks("vlx5xbwqaojyvnr68jwj5jiya", playlist_id)
    except Exception as e:
        return f"error fetching data from spotify: {e}"

    # collect track and artist data
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    rap_songs = []
    not_rap_songs = []
    artists_genres = {}

    # categorize tracks by genres
    for track in tracks:
        song_name = track['track']['name']
        for artist in track['track']['artists']:
            artist_data = sp.artist(artist['uri'])
            genres = artist_data.get('genres', [])
            if 'hip hop' in genres or 'rap' in genres:
                rap_songs.append(song_name)
            else:
                not_rap_songs.append(song_name)

            # collect genre data for plotting
            for genre in genres:
                if genre in artists_genres:
                    artists_genres[genre] += 1
                else:
                    artists_genres[genre] = 1

    # plot genre distribution and return the result
    img = plot_genre_distribution(artists_genres)

    return render_template('playlist.html', rap_songs=rap_songs, not_rap_songs=not_rap_songs, img_data=img)

if __name__ == '__main__':
    app.run(debug=True)
