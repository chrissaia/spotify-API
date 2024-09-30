from collections import UserList
import spotipy
from datalist import dataList, uriList
from spotipy.oauth2 import SpotifyClientCredentials

# Get Spotify Credentials from environment variables
spotify_id = "" // secret
spotify_secret = "" // secret

if not spotify_id or not spotify_secret:
    raise ValueError("Spotify credentials not found in environment variables.")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_id, client_secret=spotify_secret))






try:
    results = sp.user_playlist_tracks("vlx5xbwqaojyvnr68jwj5jiya", "3koK42MMEigNKPCH3mxn3o")
except Exception as e:
    print(f"Error fetching data from Spotify: {e}")

rapSong = []
not_rapSong = []



tracks = results['items']
while results['next']:
  results = sp.next(results)
  tracks.extend(results['items'])
  
for key in tracks:
  print(key['track']['name'])




'''
for key in tracks:
  temp_list = []
  for x in range(len(key['track']['artists'])):
    artist = sp.artist(str(key['track']['artists'][x]['uri'])[15:])
    print(str(key['track']['artists'][x]['uri'])[15:])
    
  with open("datalist.txt","a") as filehandle:
    filehandle.write("%s\n" % artist['genres'] + "\n")

'''
