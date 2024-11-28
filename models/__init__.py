from flask_sqlalchemy import SQLAlchemy

# Initialize the db object
db = SQLAlchemy()

# Import the models (User and Book models)
from .user import User
from .book import Book
