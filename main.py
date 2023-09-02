from fastapi import FastAPI, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

import schemas
import models


# if we don't have database it will create new 1 by using engine we created
Base.metadata.create_all(engine)


# function which will help us to access to the database and session

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



app = FastAPI()

# http://127.0.0.1:8000/docs#/ this help you to run the swagger UI as testing


#user endpoints

# get all user by using database and tables
@app.get("/")
def getUsers(session: Session = Depends(get_session)):
    users = session.query(models.User).all()
    return users


# get one user by using database and tables
@app.get("/{id}")
def getUser(id: int, session: Session = Depends(get_session)):
    user = session.query(models.User).get(id)
    return user


# post request for creating data in database
@app.post("/")
def addUser(user:schemas.User, session: Session = Depends(get_session)):
    user = models.User(name=user.name,age=user.age,phone=user.phone)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# put request by getting data in table
@app.put("/{id}")
def updateUser(id: int, user: schemas.User, session: Session = Depends(get_session)):
    userObject = session.query(models.User).get(id)
    userObject.name = user.name
    userObject.age = user.age
    userObject.phone = user.phone
    session.commit()
    return userObject

# delete request
@app.delete("/{id}")
def deleteUser(id: int, session: Session = Depends(get_session)):
    userObject = session.query(models.User).get(id)
    session.delete(userObject)
    session.commit()
    session.close()
    return "User was deleted"


#book endpoints

# get all book by using database and tables
@app.get("/book/")
def getBooks(session: Session = Depends(get_session)):
    books = session.query(models.book).all()
    return books


# get one book by using database and tables
@app.get("/book/{id}")
def getBook(id: int, session: Session = Depends(get_session)):
    book = session.query(models.book).get(id)
    return book


# post request for creating  Book data in database
@app.post("/book/")
def addBook(Book:schemas.book, session: Session = Depends(get_session)):
    Books = models.book(bookname=Book.bookname,author=Book.author,user_id=Book.user_id)
    session.add(Books)
    session.commit()
    session.refresh(Books)
    return Books


# put request by getting Book data in table
@app.put("/book/{id}")
def updateBook(id: int, Book: schemas.book, session: Session = Depends(get_session)):
    BookObject = session.query(models.book).get(id)
    BookObject.bookname = Book.bookname
    BookObject.author = Book.author
    BookObject.user_id = Book.user_id
    session.commit()
    return BookObject

# delete request
@app.delete("/book/{id}")
def deleteBook(id: int, session: Session = Depends(get_session)):
    BookObject = session.query(models.book).get(id)
    session.delete(BookObject)
    session.commit()
    session.close()
    return "book was deleted"
