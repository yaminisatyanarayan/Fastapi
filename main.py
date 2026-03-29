# import fastapi clall from mfasapi module
from fastapi import FastAPI

#create instace of fastapi
#app object is used to define all api routes
app =FastAPI()

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