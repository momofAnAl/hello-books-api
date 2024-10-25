from flask import Blueprint, abort, make_response
# from app.models.book import books

book_bp = Blueprint("book_bp", __name__, url_prefix="/books")












# @book_bp.get("")
# def get_all_books():
#     books_response = [book.to_dict() for book in books]
#     return books_response

# @book_bp.get("/<book_id>")
# def get_one_book(book_id):
#     book = validate_book(book_id)
#     return book.to_dict()


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