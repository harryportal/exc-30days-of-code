from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .user_blueprint import user
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login.html'
login.login_message = 'Please login to continue'
app.register_blueprint(user)







