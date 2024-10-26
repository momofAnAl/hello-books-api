from flask import Blueprint, abort, make_response, request
from ..db import db
from app.models.book import Book

book_bp = Blueprint("book_bp", __name__, url_prefix="/books")

@book_bp.post("")
def create_book():
    request_body = request.get_json()
    id = request_body["id"]
    title = request_body["title"]
    description = request_body["description"]
    
    new_book = Book(id=id, title=title, description=description)
    db.session.add(new_book)
    db.session.commit()
    
    response = new_book.to_dict()
    return response, 201
    
@book_bp.get("")
def get_all_books():
    query = db.select(Book).order_by(Book.id)
    books = db.session.scalars(query)
    response_body = [book.to_dict() for book in books]
    
    return response_body, 200
    


# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except ValueError:
#         response = {"message": f"book {book_id} invalid"}
#         abort(make_response(response, 400))
    
#     for book in books:
#         if book.id == book_id:
#             return book
    
#     response = {"message": f"book {book_id} not found"}
#     abort(make_response(response, 404))