from sqlalchemy import column,Integer,String,Column
from database import engine
from sqlalchemy.orm import declarative_base

Base =declarative_base()

class User(Base):
    __tablename__ ="users"
    
    id =Column(Integer,primary_key=True,index=True)
    name =Column(String)
    email =Column(String)
    password =Column(String)
Base.metadata.create_all(bind=engine)#create s