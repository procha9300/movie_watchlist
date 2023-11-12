from typing import Any
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, URLField, PasswordField
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo

''' FlaskForm will give the added functinality to protect us from CSRF attacks'''
''' CSRF: Cross-site request forgery
is an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated. 
CSRF attacks exploit the trust a Web application has in an authenticated user.'''
class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director", validators=[InputRequired()])

    year = IntegerField(
        "Year", 
        validators=[
            InputRequired(), 
            NumberRange(min=1878, message="Please enter a year in the format YYYY.")]
        )
    
    submit = SubmitField("Add Movie")


class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""
        
    def process_formdata(self, valuelist: list[Any]) -> None:
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split('\n')]
        else:
            self.data = []

class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link")

    submit = SubmitField("Submit")

class RegisterFrom(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField(
        "Password", 
        validators=[
            InputRequired(), 
            Length(min=4, 
                   max=20, 
                   message="Your password must be between 4 and 20 charaters long."
                   )
            ]
        )
    confirm_password = PasswordField(
        "Confirm Password", 
        validators=[
            InputRequired(), 
            EqualTo(
                "password",
                message="This password did not match the one in the password field."
                )
            ]
        )
    submit = SubmitField("Register")

class LoginFrom(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")