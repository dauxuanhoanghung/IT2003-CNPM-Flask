from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '12#^&*+_%&*)(*(&(*^&^$%$#((*65t87676'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/it03dbsaleapp?charset=utf8mb4" % quote(
    'Hung28122002@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
