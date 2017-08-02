from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# REPLACE YourModel with the one that you created in model.py
from model import User, Idea, Comment

engine = create_engine('sqlite:///project.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()
# new_idea = Idea(name="name1", describtion = "desc1", looking_for = 'look1',
# 	owner="own1", likes=0, category="cat1")
# session.add(new_idea)
# session.commit()

comments = session.query(Comment).all()

for comment in comments:
	print(comment)