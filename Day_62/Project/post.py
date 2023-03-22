import requests


class Post:
    def __init__(self):
        urlBlogs = "https://api.npoint.io/c790b4d5cab58020d391"
        with requests.get(url=urlBlogs) as blogs:
            blogs.raise_for_status()
            self.blogs = blogs.json()
