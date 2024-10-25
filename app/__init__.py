from flask import Flask
from .db import db, migrate
from .models import book
from .routes.book_routes import book_bp

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_book_development'

    db.init_app(app)
    migrate.init_app(app, db)

    # predefine function register_blueprints()
    app.register_blueprint(book_bp)

    return app
