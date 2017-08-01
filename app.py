# flask imports
from flask import Flask, Response, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, Idea, Comment, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
app.config["SECRET_KEY"]="malak"
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# flask-login imports
from flask_login import login_required, current_user
from login import login_manager, login_handler, logout_handler, sign_up_handler
login_manager.init_app(app)



# @app.route('/', methods=['GET','POST'])
# def sign_in():
# 	if request.method == 'GET':
# 		return render_template('sign_in.html')
# 	else :
# 		new_first_name=request.form.get('first_name')
# 		check_name=session.query(User).filter_by(firstname=new_first_name).first()
# 		new_pass=request.foem.get('password')
# 		if check_name.name==new_first_name and check_name.password==new_pass:
# 			flash('You were successfully logged in')
# 			return render_template('discover.html')
# 		else:
# 			flash('Invalid credentials')
    		

@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        sign_up_handler(request)
        return redirect(url_for('discover'))


@app.route('/discover')
@login_required
def discover():
	return render_template('discover.html')


# @app.route('/show_idea/<int:idea_id>', methods=['GET','POST'])
# def show_idea(idea_id):
#     new_idea = {"name": "idea1","description": "description1", "looking_for": "lf1"}
#     comments = [{"name": "comment"}]

#     if request.method == 'GET':
#         # new_idea=session.query(Idea).filter_by(id=idea_id).first()
        
#         return render_template('idea_profile.html',idea=new_idea, comments=comments)
#     else:
#         new_comment = request.form.get('comment')
#         comments.append(new_comment)

#         new_comment = Comment




@app.route('/show_idea/<int:idea_id>')
def show_idea():
	new_idea=session.query(idea).filter_by(id=idea_id).first()
	return render_template('idea_profile.html',idea_name=new_idea.name,creator=new_idea.owner,describtion=new_idea.describtion,likes=new_idea.likes,looking_for=new_idea.looking_for)
	

@app.route('/add_idea',methods=['GET','POST'])
@login_required
def add_idea():
    if request.method == 'GET':
        return render_template('add_idea.html')
    else:  
        new_name          = request.form.get('idea_name')
        new_describtion   = request.form.get('describtion')
        new_looking_for   = request.form.get('looking_for')
        new_idea = Idea (name= new_name,\
        				describtion=new_describtion,\
        				looking_for=new_looking_for,\
        				)

        session.add(new_user)
        session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_handler(request)


@app.route('/logout')
def logout():
  return logout_handler()


@app.route('/protected', methods=["GET"])
@login_required
def protected():
    return render_template('protected.html')

