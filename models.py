from sqlalchemy import Column, Integer, String  ,ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True)
    name = Column(String(256))
    age =Column(Integer)
    phone=Column(String)

    books=relationship("book", back_populates="users" )


class book(Base):
     __tablename__ = "books"

     book_id = Column(Integer, primary_key=True)
     bookname = Column(String)
     author = Column(String)
     user_id= Column(Integer, ForeignKey("users.user_id"))

     users=relationship("User", back_populates="books")


