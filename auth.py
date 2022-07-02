from flask import Blueprint,request,render_template,redirect,url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required
from .models import Session
from sqlalchemy import select
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html',title='Login')
    else:
        name = request.form.get('user')
        password = request.form.get('password')

        with Session() as session:
            stmt = select(User).where(User.name==name)
            user_data = session.execute(stmt).scalar()

        if not user_data:
            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user_data.password, password):
            flash('Please check your login details and try again.')
    # login_user(user_data)
    return redirect(url_for('main./'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('signUp.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Incorect Password')
            return redirect(url_for('auth.signup'))

        with Session() as session:
            stmt = select(User).where(User.name==name)
            user = session.execute(stmt).scalar()

        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        
        new_user = User(
            name=name,
            password=generate_password_hash(password, method='sha256'),
            join_date = datetime.now()
            )
        with Session() as session:
            session.add(new_user)
            session.commit()


        
        return redirect(url_for('main.home'))