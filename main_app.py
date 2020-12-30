import os
import secrets
from PIL import Image
from flask import Flask, render_template, redirect, url_for, flash, request
from forms import RegistrationForm, LoginForm, AccountUpdateForm, PostForm
from models import db
from models import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
from flask_migrate import Migrate




app = Flask(__name__)
app.config['SECRET_KEY'] = 'si'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к аккаунту нужно авторизоваться'
login_manager.login_message_category = 'info'
migrate = Migrate(app, db)



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
    posts = Post.query.all()
    return render_template('base.html', posts=posts)

 




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
        return redirect(url_for('login'))
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
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Не правильный email или пароль', "danger ")
    return render_template('login.html', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



def save_avatar(avatar):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(avatar.filename)
    avatar_name = random_hex + f_ext
    avatar_path = os.path.join(app.root_path, 'static/profile_images', avatar_name)
    avatar_size = (200, 250)
    i = Image.open(avatar)
    i.thumbnail(avatar_size)
    i.save(avatar_path)
    return avatar_name


@app.route('/account/', methods=['POST', 'GET'])
@login_required
def account():
    form = AccountUpdateForm()
    # user = User.query.get(user_id)
    if form.validate_on_submit():
        if form.avatar.data:
            avatar_file = save_avatar(form.avatar.data)
            current_user.avatar = avatar_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Данные пользователя обновлены!', 'success')
        redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.avatar.data = current_user.avatar
    avatar = url_for('static', filename='profile_images/' + current_user.avatar)
    print(avatar)
    return render_template('account1.html', form=form, avatar=avatar)




@app.route('/post/new', methods=['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        print(current_user)
        db.session.add(post)
        db.session.commit()
        flash('Пост был создал!', 'succes')
        redirect(url_for('index'))
    
    return render_template('create_post.html', form=form)




@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)




@login_required
@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    print(post_id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        # return redirect(url_for('post', post_id=post.id))
    if request.method == 'GET':
        form.title.data = post.title 
        form.content.data = post.content 
    return render_template('create_post.html', form=form, post=post)



if __name__ == "__main__":
    app.run(debug=True) 