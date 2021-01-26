from flask import Flask
from flask_mail import Mail, Message



app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'xxoce13@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'xxoce13gmail.com'
app.config['MAIL_PASSWORD'] = 'kadzama095'
mail = Mail(app)




@app.route('/')
def index():
    msg = Message('Your Login and Password', recipients=['ya.amerika-2015@yandex.ru'])
    msg.body = '''login: agfgfg' password: 1313245'''
    mail.send(msg)
    return {
        'status': True
    }


app.run(debug=True)