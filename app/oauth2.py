from email.policy import HTTP

from fastapi.security import OAuth2
from fastapi import Depends
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer 
from app import schemas
from sqlalchemy.orm import Session
from .config import settings 

OAuth2_scheme= OAuth2PasswordBearer(tokenUrl="login")

# Secret_key
# Algorithm
# Expiration time



SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode=data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_expection):
    try:

        payload=jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])

        id: str = str(payload.get("user_id"))

        if id is None:
            raise credentials_expection
        token_data = schemas.TokenData(id=id)  
    except JWTError:
        raise credentials_expection
    
    return token_data
    

def get_current_user(token: str = Depends(OAuth2_scheme), db: Session = Depends(database.get_db)):
    credentials_expection = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    token = verify_access_token(token, credentials_expection)
    user=db.query(models.User).filter(models.User.id == token.id).first()
    return user

        



