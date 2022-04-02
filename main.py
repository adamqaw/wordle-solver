from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import Greens, Yellows, AvailableLetters
import requests

API_KEY = '05a09b32-920e-4ead-8a11-fcf0a809050b'


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
    word = ''
    endpoint = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}'
    response = requests.get(endpoint)
    word = response.text
    return render_template('index.html', word=word)


@app.route('/possible-words')
def possible_words():
    return render_template('possible-words.html')


if __name__ == '__main__':
    app.run(debug=True)
