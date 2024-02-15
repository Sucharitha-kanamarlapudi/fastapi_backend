from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.user import UserCreate,ShowUser
from db.models.user import User
from db.session import get_db
from db.repository.user import create_new_user
from apis.version1.route_login import get_current_user

router = APIRouter()

@router.post('/',response_model=ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db),current_user: User =Depends(get_current_user)):
    if current_user.is_admin:
        user = create_new_user(user=user, db=db)
        return user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Sorry.. you don't have access to add the user")
