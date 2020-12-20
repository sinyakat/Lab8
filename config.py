import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class DevConfig(object):
    ENV='development'
    DEBUG=True
    SECRET_KEY = 'my-secret-key'
    CSRF_ENABLED = True
    SECRET_KEY = 'some-secret-string'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
