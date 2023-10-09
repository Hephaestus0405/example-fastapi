
from fastapi.security import oauth2
from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from .. import  models, schemas, oauth2
from sqlalchemy.orm import Session
from .. database import  engine, get_db
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(              ## "posts path operattion is repeating so we use prefix = "/posts" and for id = "/posts" +"/{id}"
    prefix= "/posts",
    tags= ["Posts"]   # This will group all the posts in api/docs and its list so you can pass and grp other related end points.
)

@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    #cursor.execute(""" SELECT * FROM posts """)
    #posts = cursor.fetchall()
    print(limit)
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).Join(models.Vote, models.Vote.post_id == models.Post.id, is_outer = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # The above "Join" is by default it will perform left inner join. 
    return  posts


# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):      #without using pydantic model
#     print(payload)
#     return {"new_post": f"title: {payload['title']} content: {payload['content']}"}


@router.post("/",status_code = status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   #cursor.execute(""" INSERT INTO  posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
   #new_post = cursor.fetchone()
   #conn.commit() # it will push the changes in database.
   new_post=models.Post(owner_id = current_user.id,**post.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return  new_post

# If you convert a pydantic model into a dictionary like new_post is a separate pydantic model ,then, we use 
#print(new_post.dict())


# We use pydantic to define schema means how our data should look like(What exact data we want from front-end to validate data)

#pydantic is a separate library its nothing to do that with fastapi.
# we want users to send title(str) and content(str) only.

@router.get("/{id}", response_model=schemas.Post)
def get_post(id : int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):    #(pydantic validation) and db session.

   #cursor.execute(""" SELECT * FROM posts WHERE id = %s""", (str(id)))
   #post = cursor.fetchone()
   post = db.query(models.Post).filter(models.Post.id == id).first()
   if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} doesnt not exit")
   return  post



@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} doesnt not exit!!")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    post_query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, Updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute(""" UPDATE  posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, (str(id))))
    #updated_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} doesnt not exit!!")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    post_query.update(Updated_post.dict(), synchronize_session=False)
    db.commit()
    return  post_query.first()
