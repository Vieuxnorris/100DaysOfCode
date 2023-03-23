import os
import smtplib

from flask import Flask, render_template, request
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

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form['name']
        email = request.form['email']
        tel = request.form['phoneNumber']
        message = request.form['messageText']
        with smtplib.SMTP("smtp.gmail.com") as gmail:
            gmail.starttls()
            gmail.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
            gmail.sendmail(from_addr=os.getenv("MY_EMAIL"),
                           to_addrs=os.getenv("MY_EMAIL"),
                           msg=f"Subject:New Message!\n\nName: {name}\nEmail: {email}\nPhone Number: {tel}\n"
                               f"Message: {message}\n")
        return render_template("contact.html", msg_sent=True)


@app.route('/post/<int:idBlog>')
def blogPost(idBlog):
    blog = BLOGS.blogs[idBlog - 1]
    return render_template("post.html", blogInfo=blog)


if __name__ == "__main__":
    app.run(debug=True)
