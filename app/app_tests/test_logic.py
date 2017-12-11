import unittest
from flask import url_for
from app.models import User

from app.app_tests.test_base import BaseTestCase


class UserViewTest(BaseTestCase):

    def test_check_user_exist(self):
        self.db.session.add(User(first_name='aaa',last_name='fff',user_id=1234))
        self.db.session.commit()

        res = self.client.post('login',data=dict(first_name='aaa',last_name='fff',user_id=1234))
        self.assert_redirects(res, url_for('index'))

    def test_login_without_id(self):
        self.db.session.add(User(first_name='aaa', last_name='fff', user_id=1234))
        self.db.session.commit()
        res = self.client.post('login', data=dict(first_name='aaa', last_name='fff'))
        self.assertEqual(res.status_code, 400)

    def test_not_auth_user(self):
        res = self.client.get('/app/manager')
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()