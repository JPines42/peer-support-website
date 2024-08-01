from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

# Signup page verification


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(
        min=2, max=20)])  # Username must be between 2-20 characters
    # Email must be valid
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=8, max=30)])  # Password must be between 8-30
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(
    ), EqualTo('password'), Length(min=8, max=30)])  # Confirming password
    submit = SubmitField('Sign Up')  # Submit to database

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            # If username is already in use
            raise ValidationError(
                "Username already taken. Please choose a different one")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            # If password is already in use
            raise ValidationError(
                "Email already taken. Please choose a different one")
