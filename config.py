import os
basedir = os.path.abspath(os.path.dirname(__file__))

""" Main Config """
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bajskorv'

    # DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

""" Different related objects depending on context (dev,test,stage,prod etc.)"""