from flask import Flask
from app.routes.book_routes import book_bp

def create_app():
    app = Flask(__name__)

    # predefine function register_blueprints()
    app.register_blueprint(book_bp)

    return app
