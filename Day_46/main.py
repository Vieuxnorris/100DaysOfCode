import os
import re
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = "2ed40ca3e8e24294ad718ca544896881"
SPOTIFY_CLIENT_SECRET = os.getenv("API_SPOTIFY")

title = []
songs = []

userInput = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

try:
    with requests.get(url=f"{URL}/{userInput}/") as playList:
        playList.raise_for_status()
        htmlScraping = playList.text
except requests.exceptions.HTTPError:
    print("ERROR HTTP")
else:
    soup = BeautifulSoup(htmlScraping, "html.parser")
    title = [str(tag.getText().strip()) for tag in soup.select(selector=".a-truncate-ellipsis")]
    author = [str(tag.getText().strip()) for tag in
              soup.select(selector=".a-truncate-ellipsis-2line")]
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                   client_secret=SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri="http://example.com",
                                                   scope="playlist-modify-private",
                                                   cache_path="token.txt"))
    for index in range(0, len(title) - 1):
        author[index] = re.sub(r'\b(Featuring|With|&)\b', ',', author[index]).replace(" ,", ",")
        print(author[index])
        results = sp.search(q=f"track:{title[index]} artist:{author[index]} year:{userInput.split('-')[0]}")
        try:
            uri = results['tracks']["items"][0]['uri']
            print(f'track    : {uri}')
        except IndexError:
            print(":-( no info track found in spotify")
        else:
            songs.append(uri)

    playlist = sp.user_playlist_create(sp.current_user()['id'], f"{userInput} Billboard {len(songs)}", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=songs)

