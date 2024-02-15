from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.user import User
from core.hasing import Hasher

def create_new_user(user: UserCreate, db: Session):
    user = User(
        email = user.email,
        password = Hasher.get_password_hash(user.password),
        is_active = True,
        is_admin = False
    )
    db.add(user)
    db.commit()
    db.refresh
    return user
