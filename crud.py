from models import User

def create_user(db,user):
    new_user =User(name=user.name,email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db):
    return db.query(User).all()