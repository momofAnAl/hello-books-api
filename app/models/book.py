from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db
  
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("author.id"))
    #author is the table
    author: Mapped[Optional["Author"]] = relationship(back_populates="books")
    
    def to_dict(self):
        #key-value pair.
        #you want to exclude fields based on some conditions
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description
        
        if self.author:
            book_as_dict["author"] = self.author.name

        return book_as_dict

    @classmethod # this decorator indicate that from_dict is a class method
#which mean it's called in the class itself(cls), not an instance of class

    def from_dict(cls, book_data):
        author_id = book_data.get("author_id")
#create a helper for creating Book instance directly from dictionary
#book_data: dictionary is expected contain keys that match columns title and description
        new_book = cls(title=book_data["title"], 
                       description=book_data["description"],
                       author_id=author_id)
        #cls refer class itself, (Book) 
        #create new_book instance with t and des values from book_data dict
        return new_book #create instance new_book from dict or Json
    
