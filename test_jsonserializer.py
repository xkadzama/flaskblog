from flask import Flask
from itsdangerous import TimedJSONWebSignatureSerializer



# app = Flask(__name__)


s = TimedJSONWebSignatureSerializer('secret', 60)

token = s.dumps({'user_id': 2}).decode('utf-8')
print(s.loads(token))

# @app.route('/')
# def index():
#     return {
#         'status': True
#     }


# app.run(debug=True)