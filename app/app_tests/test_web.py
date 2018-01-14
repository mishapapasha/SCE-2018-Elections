from app import app, db
from app.models import User, Party
from selenium import webdriver
from flask_testing import LiveServerTestCase
import time


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
        avoda = Party(u'העבודה',
                      'https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg', )
        likud = Party(u'הליכוד',
                      'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Likud_Logo.svg/250px-Likud_Logo.svg.png')
        lavan = Party(u'פתק לבן',
                      'https://www.weberthai.com/fileadmin/user_upload/01_training-elements/02.4_others/02.5_color_cards/05_color_mosaic/images/1.jpg')
        db.session.add(avoda)
        db.session.add(likud)
        db.session.add(lavan)

    def tearDown(self):
        with app.app_context():
            self.browser.close()
            del self.db
            del self.browser
            db.drop_all()



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

    def test_full_integration_selenium(self):
        with app.app_context():
            pageDelay = 3
            self.db.session.add(User(first_name='John', last_name='Vituli', user_id=123456))
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


            party = self.browser.find_element_by_id('הליכוד')
            self.browser.execute_script('arguments[0].checked = true;', party)
            submit = self.browser.find_element_by_id('submitForm')
            submit.click()
            time.sleep(3)
            popup = self.browser.find_element_by_id('confirm')
            popup.click()
            self.assertEqual(self.browser.current_url, self.get_server_url() + '/login')


