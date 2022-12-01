# forms.py - create form object

from flask_wtf import FlaskForm, RecaptchaField, Recaptcha
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    """Contact form."""

    name = StringField(
        'Name',
        validators=[DataRequired(message='Please enter your name.')]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Please enter your email address.'),
            Email(message='Not a valid email address.')
        ]
    )
    subject = StringField(
        'Subject',
        validators=[DataRequired(message='Please enter a subject.')]
    )
    body = TextAreaField(
        "Message",
        validators=[
            DataRequired(message='Please enter a message.'),
            Length(min=4, message="Your message is too short.")
        ]
    )
    recaptcha = RecaptchaField(validators=[Recaptcha(message="You're not a robot... are you?")])
    submit = SubmitField("Submit")