from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from models import db
from flask_bcrypt import Bcrypt
from models import *
# from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'si'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = db.init_app(app)
bcrypt = Bcrypt(app)
# migrate = Migrate(app, db)

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
    
    return render_template('base.html', data=base)









@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password )
        db.session.add(user)
        db.session.commit()
        flash('Аккаунт создан', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    # post = Post(title='Forest', content='a love forest', user_id='1')
    # db.session.add(post)
    # db.session.commit()

    # user = User.query.filter_by(username='Xoce').first()
    # print(user.posts)

    return render_template('login.html', form=form)

app.run(debug=True) 