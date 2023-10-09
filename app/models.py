
from enum import unique
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy.orm import relationship

class Post(Base):                      #This is sqlalchemy model.This model defines how our specfic table looks like.
    __tablename__ = "posts_one"           #sql alchemy just see in their is not table name posts_one then it will create it but, if it is their  and you update something ,then ,it will not do anything(not update anything).we have to use data migration tool like "Alembic".

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default = 'TRUE', nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    owner = relationship("User") # it  is going to fetch the user based on owner_id automatically for us.
#We are going to set-up some relationship and what it does is it automatically tells the sqlalchemy to fetch some piece of information
#based off of the relationship (above line).


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
    phone_number = Column(String)


