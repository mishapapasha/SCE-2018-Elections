from flask_testing import TestCase
from .. import app, db

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('flask_config.TestsConfiguration')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

