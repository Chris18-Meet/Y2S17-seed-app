from flask_login import UserMixin

from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash
Base = declarative_base()

class Idea(Base):
    __tablename__  = 'idea'
    id             = Column(Integer, primary_key=True)
    name           = Column(String)
    description    = Column(String)
    looking_for    = Column(String)
    owner          = Column(String)
    owner_id       = Column(Integer)
    likes          = Column(Integer)
    category       = Column(String)

    # ADD YOUR FIELD BELOW ID

class Comment(Base):
    __tablename__  = 'comment'
    id             = Column(Integer, primary_key=True)
    comment        = Column(String)
    idea           = Column(String)
    owner          = Column(String)

class User(UserMixin, Base):
    __tablename__  = 'user'
    id             = Column(Integer, primary_key=True)
    first_name     = Column(String)
    last_name      = Column(String)
    email          = Column(String)
    pw_hash        = Column(String)
    profession     = Column(String)
    linkedin_url   = Column(String)
    photo          = Column(String)
    authenticated  =Column(Boolean,default=False)

    def __repr__(self):
      return "<User: %s, password: %s>" % (
        self.email, self.pw_hash)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)