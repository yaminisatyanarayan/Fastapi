from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email:str
    password:str

class Login(BaseModel):
    username:str
    password:str