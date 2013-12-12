#-*- coding: utf-8 -*-
import time

class BaseTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        cls.driver.quit()

class AdminTestCase(BaseTestCase):
    
    def test_login(self):
        # Open the administration page
        self.driver.get('http://localhost:8000/admin/')
        self.driver.save_screenshot('admin-login.png')
        # Enter the name of the user
        self.driver.find_element_by_id('id_username').send_keys('admin')
        # Get the password input
        password = self.driver.find_element_by_id('id_password')
        # Type password
        password.send_keys('admin')
        # Submit the form
        password.submit()
        # Load page
        time.sleep(2)
        self.driver.save_screenshot('admin-welcome.png')
        # Check that welcomed
        self.assertTrue(self.driver.find_element_by_id('user-tools').text.startswith('Welcome'))


