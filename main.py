from bs4 import BeautifulSoup
import requests

year = input("What year would you like to travel to? (YYYY-MM-DD format): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

song_names = [title.getText() for title in soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")]
songs = [song.strip('\n') for song in song_names]
print(songs)

