from sqlalchemy import Column, Integer, String  ,ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Item(Base):
    __tablename__ = "items"
    
    item_id = Column(Integer, primary_key=True)
    name = Column(String(256))
    age =Column(Integer)
    phone=Column(String)

    books=relationship("book", back_populates="items" )


class book(Base):
     __tablename__ = "books"

     book_id = Column(Integer, primary_key=True)
     bookname = Column(String)
     author = Column(String)
     item_id= Column(Integer, ForeignKey("items.item_id", ondelete="cascade"))

     items=relationship("Item", back_populates="books")


