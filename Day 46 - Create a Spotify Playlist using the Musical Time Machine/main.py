import requests
from bs4 import BeautifulSoup

date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url = f'https://www.billboard.com/charts/hot-100/2023-11-25}/')
result = response.text
l1 = []
soup = BeautifulSoup(result,"html.parser")
music_list = [i.getText().strip() for i in soup.select('li ul li h3')]


from pathlib import Path

client_id = ''
client_secret = ''
redirect_uri = 'http://example.com'
scope = 'playlist-modify-public'
username = ''
cache = ''
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path=cache,
        username=username,
    )
)
user_id = sp.current_user()["id"]



song_uris = []
year = date.split("-")[0]
for song in music_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)