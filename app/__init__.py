from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    user = 'TECHIE'
    return render_template('index.html', user=user)