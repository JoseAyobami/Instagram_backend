from fastapi import Depends
from sqlalchemy.orm import Session

from passlib.context import CryptContext 
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import timedelta, datetime


from .models import User



bcrypt_context = CryptContext(schemas=["bcrypt"], deprecated="auto")
OAuth2_bearer = OAuth2PasswordBearer(tokenUrl="v1/auth/token")
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINS = 60 * 24 * 30  # 3o days



# check for existing user
async  def existing_user(db: Session, username: str, email: str):
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        return db_user
    db_user = db.query(User)

