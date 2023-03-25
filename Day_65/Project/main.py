import sqlalchemy.exc
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)
Bootstrap(app)


class bookDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


class bookForm(FlaskForm):
    bookName = StringField('book name', validators=[DataRequired()])
    authorName = StringField('author name', validators=[DataRequired()])
    ratingBook = FloatField("rating", validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Submit')


class editForm(FlaskForm):
    ratingBook = FloatField("rating", validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    all_books = bookDB.query.all()
    print(all_books)
    return render_template('index.html', books=all_books, lenBooks=len(all_books))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = bookForm()
    if form.validate_on_submit():
        try:
            new_book = bookDB(title=form.bookName.data, author=form.authorName.data, rating=form.ratingBook.data)
            db.session.add(new_book)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            print("ERROR title or author already exist")
        else:
            return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit?id=<int:id>", methods=['GET', 'POST'])
def edit(id):
    form = editForm()
    book_to_update = bookDB.query.filter_by(id=id).first()
    if form.validate_on_submit():
        book_to_update.rating = form.ratingBook.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, infoBook=book_to_update)


@app.route("/remove?id=<int:id>", methods=['GET', 'POST'])
def remove(id):
    book_to_delete = bookDB.query.filter_by(id=id).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    # try:
    #     cursor.execute(
    #         "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
    #         " author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    # except sqlite3.OperationalError:
    #     print("table books already exists")
    # finally:
    #     cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    #     db.commit()
    app.run(debug=True)
    with app.app_context():
        db.create_all()
