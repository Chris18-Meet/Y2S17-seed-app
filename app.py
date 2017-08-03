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


@app.route('/discover',methods=["GET", "POST"])
@login_required
def discover():
    if request.method == 'GET':
        ideas_here = session.query(Idea).all()
        return render_template('discover.html',ideas=ideas_here)
    else:
        search_here=request.form.get('search')
        return redirect(url_for('search',category_now=search_here))


@app.route('/my_ideas')
@login_required
def my_ideas():
    my_ideas_here=session.query(Idea).filter_by(owner_id=current_user.id).all()
    return render_template('my_ideas.html',my_ideass=my_ideas_here)


@app.route('/search/<string:category_now>', methods=["GET", "POST"])
@login_required
def search(category_now):
    category_ideas_here=session.query(Idea).filter_by(category=category_now).all()
    return render_template('search.html',category_ideas=category_ideas_here,category_name=category_now)


@app.route('/profile')
@login_required
def profile():
	return render_template('profile.html',first_name=current_user.first_name,last_name=current_user.last_name,profession=current_user.profession,linkedin_url=current_user.linkedin_url,image_url=current_user.photo)	


@app.route('/show_idea/<int:idea_id>',methods=["GET", "POST"])
def show_idea(idea_id):
        if request.method == 'GET':
            idea = session.query(Idea).filter_by(id=idea_id).first()
            comments = session.query(Comment).filter_by(idea=str(idea_id)).all()
            return render_template('idea_profile.html', idea=idea, comments =comments)
        else:
            new_comment=request.form.get('comment')
            new_idea=str(idea_id)
            new_owner=current_user.first_name
            new_idea_id=current_user.id
            new_comment=Comment(comment=new_comment,idea=new_idea,owner=new_owner)
            session.add(new_comment)
            session.commit()
            return redirect(url_for('show_idea',idea_id=idea_id))


@app.route('/add_idea',methods=['GET','POST'])
@login_required
def add_idea():
    if request.method == 'GET':
        return render_template('add_idea.html')
    else:  
        new_name          = request.form.get('idea_name')
        new_description   = request.form.get('description')
        new_looking_for   = request.form.get('looking_for')
        new_category      = request.form.get('category')
        new_idea = Idea(owner_id=current_user.id,name= new_name,description=new_description,looking_for=new_looking_for,owner=current_user.first_name,likes=0,category=new_category)

        session.add(new_idea)
        session.commit()
        return redirect(url_for('discover'))


############ LOGIN ############
@app.route('/sign_in', methods=['GET', 'POST'])
def login():
	return login_handler(request)


@app.route('/logout')
def logout():
	return logout_handler()


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        sign_up_handler(request)
        return redirect(url_for('discover'))
