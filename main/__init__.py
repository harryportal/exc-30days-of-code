from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from user_blueprint import user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app.register_blueprint(user)

@app.route('/home')
def home():
    name = 'TECHIE'
    return render_template('index.html', user=name)

@app.route('/home/<string:name>')
def user(name):
    return render_template('index.html', user=name)


