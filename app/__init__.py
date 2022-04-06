from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    name = 'TECHIE'
    return render_template('index.html', user=name)

@app.route('/home/<string:name>')
def user(name):
    return render_template('index.html', user=name)


