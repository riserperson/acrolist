import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ozymandias'
    UPLOAD_FOLDER = os.getcwd() + '/uploads/'
    ALLOWED_EXTENSIONS = set(("doc","pdf","csv","txt"))
