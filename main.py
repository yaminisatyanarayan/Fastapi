# import fastapi clall from mfasapi module
from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
#create instace of fastapi
#app object is used to define all api routes
app =FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #allow all (for dev)
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    name:str =Field(...,min_length=3)
    price:float =Field(...,gt=0)
    is_available:bool
    description:Optional[str]=None
    
    
def get_current_user():
    return "current user" 
# Dependency function

#route home
@app.get("/")
def read(user=Depends(get_current_user)):
    return {"message":user} #basic health check

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

@app.middleware("http")
async def log_requests(request, call_next):
    print("Request received")
    response = await call_next(request)
    print("Response sent")
    return response