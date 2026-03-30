from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas,auth
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

router = APIRouter()

oauth2_scheme =OAuth2PasswordBearer(tokenUrl='login')

@router.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# REGISTER
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# LOGIN
@router.post("/login")
def login(user: schemas.Login, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.username)

    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_token({"sub": db_user.email})
    return {"access_token": token}


# PROTECTED ROUTE
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/protected")
def protected(user=Depends(get_current_user)):
    return {"message": "Access granted", "user": user}