from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas

router = APIRouter()

@router.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)