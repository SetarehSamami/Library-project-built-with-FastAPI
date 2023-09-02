from pydantic import BaseModel


class Item(BaseModel):
    name: str
    age: int
    phone: str

     
class book(BaseModel):
    bookname: str
    author: str
    item_id: int
    