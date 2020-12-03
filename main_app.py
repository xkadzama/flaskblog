from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm
from models import db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'si'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)

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
    db.create_all()
    return render_template('base.html', data=base)









@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Аккаунт создан', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


app.run(debug=True)