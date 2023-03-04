import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

with requests.get(url=URL) as htmlFile:
    htmlFile.raise_for_status()
    response = htmlFile.text

movies = []

soup = BeautifulSoup(response, "html.parser")
soupMovies = soup.find_all(name="h3", class_="title")

for tag in soupMovies[::-1]:
    movies.append(tag.getText())

with open("bestMovies", 'w', encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

