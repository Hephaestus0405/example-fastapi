
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor   # to import column name we use import statement
import time # we want to wait to reconnect.
from .config import settings

SQLALCHEMY_DATABASE_URL =  f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


# Connection with database may fail due to many reasons so we use try statements:

# host = i.p. address, database to connect, username and password we want to connect to.

#while True:

    #try:
        #conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='1090', cursor_factory=RealDictCursor)
       # cursor = conn.cursor()
       # print("Database connection was successfull!!")
      #  break
   # except Exception as error:
        #print("Connecting to Database failed!!")
      #  print("Error :", error)
       # time.sleep(2)
