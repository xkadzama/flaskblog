from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
import email_validator
from models import *
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class RegistrationForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    email =  StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')


    def validate_username(self, username):
        check_user = User.query.filter_by(username=username.data).first()
        if check_user:
            raise ValidationError('Такой логин существует!')

    def validate_email(self, email):
        check_user = User.query.filter_by(email=email.data).first()
        if check_user:
            raise ValidationError('Такой Email существует!')





class LoginForm(FlaskForm):
    email =  StringField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Запомнить')
    submit = SubmitField('Войти')



class AccountUpdateForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    email =  StringField('Email', validators=[DataRequired(), Email()])
    avatar = FileField('Фото профиля', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    # password = PasswordField('Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Обновить')


    def validate_username(self, username):
        if username.data != current_user.username:
            check_username = User.query.filter_by(username=username.data).first()
            if check_username:
                raise ValidationError('Такой логин существует!')

    def validate_email(self, email):
        if email.data != current_user.email:
            check_email = User.query.filter_by(email=email.data).first()
            if check_email:
                raise ValidationError('Такой Email существует!')




