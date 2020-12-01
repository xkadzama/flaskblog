from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'si'



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




# @app.route('/about')
# def about():
#     return render_template('about.html')




@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Аккаунт создан', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


app.run(debug=True)