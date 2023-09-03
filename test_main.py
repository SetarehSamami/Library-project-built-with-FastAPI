from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


import pytest
import main

from database import Base
from main import app, get_session



SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_session():
    try:
        session = TestingSessionLocal()
        yield session
    finally:
        session.close()


app.dependency_overrides[get_session] = override_get_session

client = TestClient(main.app)

@pytest.fixture
def setup(self):
    self.name="setareh"
    self.age="19"
    self.phone="091234567890"
    self.user_id="1"
    self.bookname="harry potter"
    self.author="J. K. Rowling"
    self.book_id=1
    self.user_id=1


#usertest

def test_postUsers():
    response = client.post(
        "/",json={"name": "setareh",
        "age": "19",
        "phone":"091234567890"}
    )
    assert response.status_code == 200
    assert response.json() == {"user_id": 1,
        "name": "setareh",
        "age": 19,
        "phone": "091234567890"
    }

def test_getUser():
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1,
        "name": "setareh",
        "age": 19,
        "phone": "091234567890"
    }
    

def test_getUsers():
    response = client.get("/")
    assert response.status_code== 200
    assert response.json() ==[{"user_id": 1,
        "name": "setareh",
        "age": 19,
        "phone": "091234567890"
    }]

def test_putuser():
    response = client.put("/1",json={"name": "setare",
        "age": "19",
        "phone":"091234567890"})
    assert response.status_code == 200
    assert response.json() == {
    }

def test_deleteuser():
    response = client.delete("/1")
    assert response.status_code == 200
    assert response.json() == "User was deleted"
    



#booktest


def test_postbooks():
    response = client.post(
        "/book/",json={"bookname":"harry potter",
        "author":"J. K. Rowling",
        "user_id":1})
    assert response.status_code == 200
    assert response.json() == {"bookname":"harry potter",
        "author":"J. K. Rowling",
        "user_id":1,
        "book_id":1
    }

def test_getbook():
    response = client.get("/book/1")
    assert response.status_code == 200
    assert response.json() == {"bookname":"harry potter",
        "author":"J. K. Rowling",
        "user_id":1,
        "book_id":1
    }
    

def test_getbooks():
    response = client.get("/book/")
    assert response.status_code== 200
    assert response.json() ==[{"bookname":"harry potter",
        "author":"J. K. Rowling",
        "user_id":1,
        "book_id":1
    }]

def test_putbook():
    response = client.put("/book/1",json={"bookname":"harry potter",
        "author":"J. Rowling",
        "user_id":1})
    assert response.status_code == 200
    assert response.json() == {
    }
def test_deletebook():
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json() == "book was deleted"
    




    