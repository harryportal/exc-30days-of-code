from main.user_blueprint import user
from flask import request
from models import User
from passlib.apps import custom_app_context as hash_password
from models import db
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, login_required


#route can only accessed my Login User
@login_required
@user.route('/home/<string:name>')
def user(name):
    return render_template('index.html', user=name)


@user.route('/home')
def home():
    name = 'TECHIE'
    return render_template('index.html', user=name)


@user.route('/signup', methods=['GET', 'POST'])
def signup():
    user_data = request.form
    if user_data:
        check_mail = User.query.filter_by(email=user_data['email']).first()
        if check_mail:
            flash('An account with email Exists!')
            return redirect(url_for('.signup'))
        hashed_password = hash_password.hash(user_data)
        new_user = User(name=user_data['name'], email=user_data['email'], password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('signup.html')


@user.route('/login', methods=['GET', 'POST'])
def login():
    user_data = request.form
    if user_data:
        user = User.query.filter_by(email=user_data['email']).first()
        if user and user.verify_password(user_data['password']):
            login_user(user)
            """ redirects to a requested page if it initially exists"""
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('.user', name=user.name))
        else:
            flash('Incorrect Login details!')
            return redirect(url_for('.login'))
    return render_template('login.html')
