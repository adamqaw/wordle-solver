from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Greens(FlaskForm):
    letter = StringField()
    submit = SubmitField()


class Yellows(FlaskForm):
    letter = StringField()
    submit = SubmitField()


class AvailableLetters(FlaskForm):
    list_of_letters = StringField()
    submit = SubmitField()
