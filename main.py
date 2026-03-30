# import fastapi clall from mfasapi module
from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
#create instace of fastapi
#app object is used to define all api routes
app =FastAPI()

class Product(BaseModel):
    name:str =Field(...,min_length=3)
    price:float =Field(...,gt=0)
    is_available:bool
    description:Optional[str]=None
    

#route home
@app.get("/")
def home():
    return {"hey,its my fast api learning"} #basic health check

@app.get("/user/{id}")#path parameter 
def get_user(id:int):# id directly taken from url (required)
    return {"user ID": id}

@app.get("/search/")#query parameter 
def search(q:str =None):
    return{"query:q"}#optionle 

#test

@app.post("/product",response_model=Product)
def create_product(product:Product): #api data receive data from request body and validate using pydantic model
    return product