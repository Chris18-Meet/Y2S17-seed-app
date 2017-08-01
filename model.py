from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Idea(Base):
    __tablename__  = 'Ideas'
    id             = Column(Integer, primary_key=True)
    name           = Column(String)
    describtion    = Column(String)
    looking_for    = Column(String)
    owner          = Column(String)
    likes          = Column(Integer)
    category       = Column(String)

    # ADD YOUR FIELD BELOW ID

class Comment(Base):
    __tablename__  = 'Comment'
    id             = Column(Integer, primary_key=True)
    comment        = Column(String)
    idea           = Column(String)
    owner          = Column(String)

class User(Base):
    __tablename__  = 'Users'
    id             = Column(Integer, primary_key=True)
    first_name     = Column(String)
    last_name      = Column(String)
    email          = Column(String)
    password       = Column(String)
    profession     = Column(String)
    linkedin_url   = Column(String)
    photo          = Column(String)

    # IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel