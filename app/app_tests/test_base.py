from flask_testing import TestCase
from app import app, db

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('flask_config.TestsConfiguration')
        return app

    def setUp(self):
        db.create_all()
        self.db = db
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()


    def tearDown(self):
        del self.client
        del self.db
        self.app_context.pop()
        db.session.remove()
        db.drop_all()