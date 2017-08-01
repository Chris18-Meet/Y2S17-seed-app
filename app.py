# flask imports
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, Idea, Comment,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/', methods=['GET','POST'])
def sign_in():
	if request.method == 'GET':
		return render_template('sign_in.html')
	else :
		new_first_name=request.form.get('first_name')
		check_name=session.query(User).filter_by(firstname=new_first_name).first()
		new_pass=request.foem.get('password')
		if check_name.name==new_first_name and check_name.password==new_pass:
			flash('You were successfully logged in')
			return render_template('discover.html')
		else:
			flash('Invalid credentials')
    		


@app.route('/sign_up')
def sign_up():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        new_first_name    = request.form.get('firstname')
        new_last_name     = request.form.get('lastname')
        new_pass          = request.form.get('pass')
        new_profession    = request.form.get('profession')
        new_linkedin_account = request.form.get('linkedin_account')
        new_user = User (first_name=new_first_name,\
                         last_name= new_last_name,\
    	                 password= new_pass,\
    	                 profession=new_profession,\
    	                linkedin_account=new_linkedin_account)

        session.add(new_user)
        session.commit()

