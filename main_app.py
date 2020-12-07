from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from models import db
from models import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user
# from flask_migrate import Migrate




app = Flask(__name__)
app.config['SECRET_KEY'] = 'si'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# migrate = Migrate(app, db)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
base = [
    {
        'title': 'Animal near me',
        'date': '13 October',
        'count_comments': '13',
        'post': 'Animal gfgfkgjgj jfgj fg jfgj fjg jfgj'
    }, 
    {
        'title': 'Animal near me',
        'date': '13 October',
        'count_comments': '13',
        'post': 'Animal gfgfkgjgj jfgj fg jfgj fjg jfgj'
    },
    {
        'title': 'Animal near me',
        'date': '13 October',
        'count_comments': '13',
        'post': 'Animal gfgfkgjgj jfgj fg jfgj fjg jfgj'
    }
]

@app.route('/')
def index():
    return render_template('base.html', data=base, current_user=current_user)

 




@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Один из вариантов выброса ошибки в случае если такой пользователь уже существует
        # check_user = User.query.filter_by(username=form.username.data, email=form.email.data).first()
        # if check_user is None:
        #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #     user = User(username=form.username.data, email=form.email.data, password=hashed_password )
        #     db.session.add(user)
        #     db.session.commit()
        # else:
        #     return redirect(url_for('index'))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password )
        db.session.add(user)
        db.session.commit()
        flash('Аккаунт создан', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # post = Post(title='Forest', content='a love forest', user_id='1')
    # db.session.add(post)
    # db.session.commit()

    # user = User.query.filter_by(username='Xoce').first()
    # print(user.posts)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Не правильный email или пароль', "danger ")
    return render_template('login.html', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True) 