from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]

def to_dict(self):
    return dict(
        id=self.id,
        title=self.title,
        description=self.description    
    )

        
# books = [
#     Book(1, "The Gifts of Imperfection", "Encourages readers to be kinder to themselves, and to accept imperfections"),
#     Book(2, "You Are a Badass", "Overcome doubts and fears that hold them back from living the life they desire"),
#     Book(3, "Essentialism: The Disciplined Pursuit of Less", "Say no to unnecessary obligations, and reclaim your time for truly important thing")
# ]

