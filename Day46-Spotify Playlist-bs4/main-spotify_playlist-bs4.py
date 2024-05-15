from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Constants.
SPOTIFY_URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "281d21933308415185509c8fc757df5c"
CLIENT_SECRET = "8120610be33744569b13398334c744d2"

# Input from user for chosen date.
date_input = input("--> Date (YYYY-MM-DD): ")

# Get request from URL.
response = requests.get("https://www.billboard.com/charts/hot-100/" + date_input)

# Plain text of URL HTML file.
web_page = response.text

# Parse the HTML file.
soup = BeautifulSoup(web_page, "html.parser")

# Create bs4 object containing selectors.
song_list = soup.select(selector="ul li ul li h3")

song_number = 1

# Gets string inside each bs4 object. 
for song in song_list:
    song = song.get_text().strip()
    # print(str(song_number) + ". " + song)
    song_number += 1

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Josh", 
    )
)
user_id = sp.current_user()["id"]

print(user_id)

