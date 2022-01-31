import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# User's must use their own environmental variables
load_dotenv()
SP_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SP_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

year = input("What year would you like to travel to? (YYYY-MM-DD format): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

songs = [title.getText().strip('\n') for title in soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SP_CLIENT_ID,
    client_secret=SP_CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
