import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# create the extension
db = SQLAlchemy()
# create the app

# configure the SQLite database, relative to the app instance folder

# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()

# Create a record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

#Read all records

with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    print(result)

print("-------------")
# Read a certain record
print("-------------")
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalars()
    print(book)

print("-------------")

# update a certain record by query

with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalars()
    book_to_update.title = "Harry potter and the chamber of secrets"
    db.session.commit()
    book = db.session.execute(db.select(Book).where(Book.title == "Harry potter and the chamber of secrets")).scalar()
    print(book)

print("-------------")

# update a record by primary key

book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_update.title = "Harry potter and the goblet of fire"
    db.session.commit()
    book = db.session.execute(db.select(Book.title).where(Book.title == "Harry potter and the goblet of fire"))
    print(book)

print("-------------")

# Delete a record by primary key

book_id = 1
with app.app_context():
    book_to_delete = db.session.execute((db.select(Book).where(Book.id == book_id))).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()

# Create a table in this database called books.
#
# The books table should contain 4 fields: id, title, author and rating. The fields should have the same limitations as before e.g. INTEGER/FLOAT/VARCHAR/UNIQUE/NOT NULL etc.
#
# Provide the Flask "app context" and create the schema in the database.
#
# Again, with the flask app context, create a new entry in the books table that consists of the following data:


#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()