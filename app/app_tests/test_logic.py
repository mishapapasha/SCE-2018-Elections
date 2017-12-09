import os
import unittest
from flask import url_for
from app.models import User
from app.app_tests.test_base import BaseTestCase




basedir = os.path.abspath(os.path.dirname(__file__))

class UserViewTest(BaseTestCase):

    def test_login_without_ID(self):
        pass


    def test_login_not_exists(self):
        User(first_name='aaa', last_name='fdas',user_id=64356)

        form = {}
        form['first_name'] = 'John'
        form['last_name'] = 'Vituli'
        form['user_id'] = '123456'


        response = self.client.post(url_for('login',content_type= 'application/x-www-form-urlencoded',
                                            data=dict(form)))

        self.assert_redirects(response,url_for('index'))


if __name__ == '__main__':
    unittest.main()
