from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.book import Book

book_bp = Blueprint("book_bp", __name__, url_prefix="/books")

@book_bp.post("")
def create_book():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]
    
    new_book = Book(title=title, description=description)
    db.session.add(new_book) 
    db.session.commit()# until we do this commit, the row will be added to db and show record
    
    response = new_book.to_dict()
    return response, 201
    
@book_bp.get("")
def get_all_books():
    query = db.select(Book).order_by(Book.id)
    books = db.session.scalars(query)
    response_body = [book.to_dict() for book in books]
    
    return response_body, 200
    
@book_bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_book(book_id)
    
    return book.to_dict()

@book_bp.put("/<book_id>")
def update_one_book(book_id):
    book = validate_book(book_id)
    request_body = request.get_json()
    
    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()
    
    return Response(status=204, mimetype="application/json")
    #using Response constructor

@book_bp.delete("/<book_id>")
def delete_one_book(book_id):
    book = validate_book(book_id)
    
    db.session.delete(book) # live connection to database, I want to add, update, delete 
    
    db.session.commit()# transaction, allow group all changes happens together or not at all
    
    return Response(status=204, mimetype="application/json")
    
    

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"book {book_id} invalid"}
        abort(make_response(response, 400))
    
    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query) #returns a ScalarResult object instead of an actual Book object 
    # book = db.session.execute(query).scalars().first() 
    #sequence will retrieve the Book object itself instead of returning a ScalarResult object. 
    #.scalars() extracts the actual model objects from the result, 
    # and .first() retrieves the first result (or None if there are no matches).
    
    if not book:
        response = {"message": f"book {book_id} not found"} 
        abort(make_response(response, 404))
        
    return book
    