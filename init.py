from flask import Flask, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import DevConfig
from flask_session import Session
from datetime import datetime

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
Session(app)

def login_user(username):
    session['username'] = username
    session['user_ip'] = request.remote_addr
    session['login_time'] = datetime.utcnow()

def logout_user():
    session.pop('username',None)
    session.pop('user_ip',None)
    session.pop('login_time',None)
    return redirect(url_for('index'))
