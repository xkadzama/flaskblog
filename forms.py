from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
import email_validator
from models import *


class RegistrationForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    email =  StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')


    def validate_username(self, username):
        check_user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такой логин существует!')

    def validate_username(self, email):
        check_user = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Такой Email существует!')





class LoginForm(FlaskForm):
    email =  StringField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Запомнить')
    submit = SubmitField('Регистрация')
