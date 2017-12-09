import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfiguration(object):
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'SCE'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestsConfiguration(BaseConfiguration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  + os.path.join(basedir + '/app/app_tests', 'test.db')
