from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    phone: str

     
class book(BaseModel):
    bookname: str
    author: str
    user_id: int
    