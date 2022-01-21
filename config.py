import os


class Config(object):
    SECRET_KEY = '345fe1722edfee6c073b94e01d1e6310e2b4c199'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
