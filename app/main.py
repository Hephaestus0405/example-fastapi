

from fastapi import FastAPI
from . import models
from . database import  engine
from .routers import post, user, auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine) # isse models (or table create hoga database mai)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(post.router)  # we are including the routers of post.
app.include_router(user.router) 
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Welcome to my api !!!!"}

