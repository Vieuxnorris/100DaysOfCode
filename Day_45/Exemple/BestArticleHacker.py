from bs4 import BeautifulSoup
import requests

link = []
name = []

with requests.get(url="https://news.ycombinator.com/") as hackerNews:
    response = hackerNews.text

soup = BeautifulSoup(response, "html.parser")
classTitleline = soup.find_all(name="span", class_="titleline")
classScore = soup.find_all(name="span", class_="score")
for tag in classTitleline:
    link.append(tag.find_next(name="a").get("href"))
    name.append(tag.find_next(name="a").getText())

upVotes = [int(score.getText().split(' ')[0]) for score in classScore]

maxScore = max(upVotes)
maxScoreIndex = upVotes.index(maxScore)

print(link[maxScoreIndex])
print(name[maxScoreIndex])
print(upVotes[maxScoreIndex])



