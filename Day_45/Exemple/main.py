from bs4 import BeautifulSoup


with open("website.html", "r", encoding="utf-8") as htmlFile:
    file = htmlFile.read()

soup = BeautifulSoup(file, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

contents = soup.find_all(name="a")

# tagString = [tag.get("href") for tag in contents]
# print(tagString)

# heading = soup.find(name="h1", id="name")
# print(heading)

sectionHeading = soup.find(name="h3", class_="heading")
print(sectionHeading.getText())
print(sectionHeading.get("class"))
print(sectionHeading.name)

companyUrl = soup.select_one(selector="p a")
name = soup.select_one(selector="#name")
print(companyUrl)
print(name)

heading = soup.select(selector=".heading")
print(heading)
