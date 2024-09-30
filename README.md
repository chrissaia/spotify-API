# spotify-API
## Spotify Playlist Analyzer Web App

/* This is a Flask-based web application that interacts with the Spotify API to fetch playlist data and visualize it based on different metrics like genre distribution, artist popularity, and more. The app also allows users to export playlist data into a CSV file and visualize data using charts. /*

### Features
Fetches playlist data from the Spotify API using playlist ID.
Organizes tracks by artist, genre, and popularity.
Exports playlist data to a CSV file.
Visualizes genre distribution using bar charts generated with Matplotlib.
Sorts tracks based on multiple metrics such as genre and popularity.
Caches results to reduce API calls for repeated playlist requests.

### Technologies
Backend: Flask (Python)
Frontend: HTML5, CSS3
API: Spotify Web API (Spotipy for Python integration)
Visualization: Matplotlib
Data Storage: CSV

### Installation
Prerequisites
Python 3.7+
A Spotify Developer account to get API credentials (client ID and secret). You can create one at Spotify Developer Dashboard.
Clone the Repository
```
git clone https://github.com/your-username/spotify-playlist-analyzer.git
cd spotify-playlist-analyzer
```
Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
Install Dependencies
Install the required dependencies using pip:
```
pip install -r requirements.txt
```

Set Up Environment Variables
You will need to set your Spotify API credentials in an .env file.

Create a .env file in the root directory and add your credentials like this:
```
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
```
The app will be running on http://127.0.0.1:5000/.

### Usage
Open the web app in your browser by navigating to http://127.0.0.1:5000/.
Enter the Spotify playlist ID that you want to analyze.
View the list of rap and non-rap songs based on genres fetched from Spotify.
Download the playlist data as a CSV file.
View a bar chart visualizing the genre distribution of the playlist.
