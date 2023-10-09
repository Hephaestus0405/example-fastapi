from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from .. import  models, schemas, utils
from sqlalchemy.orm import Session
from .. database import  engine, get_db


router = APIRouter(       ## "user path operattion is repeating so we use prefix = "/user" and for id = "/user" +"/{id}"
    prefix="/users",
    tags= ["Users"] # This will group all the users in api/docs.
)

@router.post("/",status_code = status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
   
   # hashing the password and retriving from => user.password

   hashed_password = utils.hash(user.password)
   user.password = hashed_password # update pydantic model
   
   new_user=models.User(**user.dict())
   db.add(new_user)
   db.commit()
   db.refresh(new_user)

   return new_user



# Retriving the specific information about the user based on id.

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"user with id: {id} doesn't exist")
    
    return user






