from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary

app = Flask(__name__)
app.secret_key = '12#^&*+_%&*)(*(&(*^&^$%$#((*65t87676'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/it03dbsaleapp?charset=utf8mb4" % quote(
    'Hung28122002@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
cloudinary.config(cloud_name='dexvnphga', api_key='388299334739685', api_secret='rl5C5v_zZp_OEEB1IunCoRou82w')

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'vi'
