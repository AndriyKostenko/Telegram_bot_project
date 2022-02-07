import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TBOT_TOKEN = '5075706698:AAGFVZzWp0hZ4IEuyg0SnI71hy2NDXDuQPA'
    APP_URL = 'https://telegramsportbot.herokuapp.com/'


