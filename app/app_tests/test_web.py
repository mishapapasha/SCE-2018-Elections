from app.models import User
from selenium import webdriver
from app import app, db
from flask_testing import LiveServerTestCase
import requests

class UITestLiveServer(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('flask_config.TestsConfiguration')
        app.config['LIVESERVER_PORT'] = 5555
        app.config['LIVESERVER_TIMEOUT'] = 1000
        self.db = db
        with app.app_context():
            self.browser = webdriver.PhantomJS()
        return app

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        with app.app_context():
            self.browser.close()
            del self.db
            del self.browser
            db.drop_all()


    def test_server_is_up_and_running(self):
        with app.app_context():
            response = requests.get(self.get_server_url())
            self.assertEqual(response.status_code, 200)


    def test_user_without_id_selenium(self):
        with app.app_context():
            self.db.session.add(User(first_name='John', last_name='Vituli', user_id=123456))
            self.db.session.commit()

            self.browser.get(self.get_server_url())
            first_name = self.browser.find_element_by_id('first_name')
            last_name = self.browser.find_element_by_id('last_name')
            submit = self.browser.find_element_by_id('submit')

            first_name.send_keys('John')
            last_name.send_keys('Vituli')
            submit.click()


            self.assertEqual(self.browser.current_url,self.get_server_url() + '/login?next=%2F')

    def test_user_not_exist_selenium(self):
        with app.app_context():
            self.db.session.add(User(first_name='Johnn', last_name='Vituli', user_id=123456))
            self.db.session.commit()
            self.browser.get(self.get_server_url())
            first_name = self.browser.find_element_by_id('first_name')
            last_name = self.browser.find_element_by_id('last_name')
            user_id = self.browser.find_element_by_id('user_id')
            submit = self.browser.find_element_by_id('submit')

            first_name.send_keys('John')
            last_name.send_keys('Vituli')
            user_id.send_keys(123456)
            submit.click()

            self.assertEqual(self.browser.current_url, self.get_server_url() + '/login?next=%2F')

    def test_not_auth_user_selenium(self):
        with app.app_context():
            self.browser.get(self.get_server_url() + '/app/manager')
            self.assertEqual(self.browser.title, '404 Not Found')




