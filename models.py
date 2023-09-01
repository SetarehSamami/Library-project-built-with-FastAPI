from sqlalchemy import Column, Integer, String
from database import Base



class Item(Base):
    __tablename__ = "items"
    
    ithem_id = Column(Integer, primary_key=True)
    name = Column(String(256))
    age =Column(Integer)
    phone=Column(String)
