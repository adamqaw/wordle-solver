from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import Greens, Yellows, AvailableLetters
import requests

API_KEY = ''
endpoint = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'
headers = {
    "word": "",
    "key": API_KEY,
           }

response = requests.get(endpoint, params=headers)


def create_app():
    application = Flask(__name__)
    Bootstrap(application)
    return application


app = create_app()
app.config['SECRET_KEY'] = 'asdfdgr12qerfwdw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wordle.db'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
