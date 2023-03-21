from flask import Flask, render_template
from post import Post

app = Flask(__name__)
BLOGS = Post()


@app.route('/')
def home():
    return render_template("index.html", blogs=BLOGS.blogs)


@app.route('/index.html')
def index():
    return render_template("index.html", blogs=BLOGS.blogs)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:idBlog>')
def blogPost(idBlog):
    blog = BLOGS.blogs[idBlog - 1]
    return render_template("post.html", blogInfo=blog)


if __name__ == "__main__":
    app.run()
