import email
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime    # This is for created_at datatype.
from typing import Optional
class PostBase(BaseModel):    #pydantic model or schemas
    title: str
    content: str
    published: bool = True   # if user doesnt provide a value its gives a default value true.


class PostCreate(PostBase):      # All the values or fields of PostBase class are inherited to CreatePost class. 
   pass



class UserOut(BaseModel):                 #Response to user
    id: int
    email: EmailStr
    created_at: datetime


    class Config:
        orm_mode = True 
# Now we are handling data send to user or Response by making schema.


#class PostOut(PostBase):
    #  Post: Post
    #  votes: int

class Post(PostBase):               #Response          
    id: int       
    created_at: datetime 
    owner_id: int
    owner: UserOut # we are going to return pydantic model.
    class Config:
        orm_mode = True 
                              
      

class UserCreate(BaseModel):
    email: EmailStr
    password: str


                    

class UserLogin(BaseModel):
    email: EmailStr
    password: str                                                   
    

class Token(BaseModel):    # Schema response for Token.
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None    # Schema for data = user_id

