from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    getBlogs = Post()
    return render_template("index.html", blogsInfos=getBlogs.blogs)


@app.route('/post/<int:idBlog>')
def getPost(idBlog):
    blog = Post().blogs[idBlog - 1]
    return render_template("blog.html", blogInfos=blog)


if __name__ == "__main__":
    app.run(debug=True)
