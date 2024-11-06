import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
from app.models.book import Book
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all() # recreate a tests database tables in an empty state at the start of test
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    book_1 = Book(title="To Kill a Mockingbird", description="A novel by Harper Lee published in 1960.")
    book_2 = Book(title="Atomic Habits", description=" A guide on building good habits and breaking bad ones to transform your life.")
    
    db.session.add_all([book_1, book_2])
    db.session.commit()
    
    return [book_1, book_2]