import os
import requests
import sqlalchemy.exc

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///best-Movie.db'
db = SQLAlchemy(app)
Bootstrap(app)

URL = "https://api.themoviedb.org/3"
API_KEY = os.getenv("API_KEY")


class editMovie(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField("Your review", validators=[DataRequired()])
    submit = SubmitField("Done")


class addMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class dbMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


@app.route("/update?id=<int:idMovie>", methods=['GET', 'POST'])
def update(idMovie):
    form = editMovie()
    book_to_update = dbMovie.query.filter_by(id=idMovie).first()
    if form.validate_on_submit():
        book_to_update.rating = form.rating.data
        book_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/remove?id=<int:idMovie>", methods=['GET', 'POST'])
def remove(idMovie):
    book_to_delete = dbMovie.query.filter_by(id=idMovie).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/select?movie=<idMovie>", methods=['GET', 'POST'])
def select(idMovie):
    param = {
        "api_key": API_KEY,
    }
    with requests.get(url=f"{URL}/movie/{idMovie}", params=param) as infoMovie:
        infoMovie.raise_for_status()
        jsonMovie = infoMovie.json()
        try:
            new_movie = dbMovie(
                title=jsonMovie["original_title"],
                year=int(jsonMovie["release_date"].split("-")[0]),
                rating=0.0,
                ranking=0,
                description=jsonMovie["overview"],
                review="None",
                img_url=f"https://image.tmdb.org/t/p/w500{jsonMovie['poster_path']}"
            )
            db.session.add(new_movie)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            print("ERROR movie already exist")
        else:
            return redirect(url_for('home'))
        return redirect(url_for('add'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = addMovie()
    if form.validate_on_submit():
        param = {
            "api_key": API_KEY,
            "query": form.title.data
        }
        with requests.get(url=f"{URL}/search/movie", params=param) as infoMovie:
            infoMovie.raise_for_status()
            listMovies = [movie for movie in infoMovie.json()['results']]
        return render_template('select.html', movies=listMovies)
    return render_template("add.html", form=form)


@app.route("/")
def home():
    try:
        movies = dbMovie.query.order_by(dbMovie.rating).all()
        for i in range(len(movies)):
            movies[i].ranking = len(movies) - i
        db.session.commit()
    except sqlalchemy.exc.OperationalError:
        print("DB not create")
    else:
        return render_template("index.html", movies=movies)
    db.create_all()
    movies = dbMovie.query.all()
    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()
