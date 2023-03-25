from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    db.create_all()
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

    all_books = Book.query.all()
    book = Book.query.filter_by(title="Harry Potter").first()

    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

    book_id = 1
    book_to_delete = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

    # book_id = 1
    # book_to_delete = Book.query.filter_by(title="Harry Potter").first()
    # db.session.delete(book_to_delete)
    # db.session.commit()
    return "salut"

if __name__ == "__main__":
    app.run(debug=True)