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



# get all item by using database and tables
@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items


# get one item by using database and tables
@app.get("/{id}")
def getItem(id: int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item


# post request for creating data in database
@app.post("/")
def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(name=item.name,age=item.age,phone=item.phone)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


# put request by getting data in table
@app.put("/{id}")
def updateItem(id: int, item: schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.name = item.name
    itemObject.age = item.age
    itemObject.phone = item.phone
    session.commit()
    return itemObject

# delete request
@app.delete("/{id}")
def deleteItem(id: int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return "Item was deleted"

