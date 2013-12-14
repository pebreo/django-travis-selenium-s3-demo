#-*- coding: utf-8 -*-
import time
from django.test import LiveServerTestCase
from django.conf import settings
#from splinter import Browser
from selenium import webdriver


# class GridTestcase(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.browser = Browser()  #'remote', **settings.SELENIUM_GRID)
#         super(GridTestcase, cls).setUpClass()

#     @classmethod
#     def tearDownClass(cls):
#         cls.browser.quit()
#         super(GridTestcase, cls).tearDownClass()


class BaseTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        cls.driver.quit()

class PollsTestCase(BaseTestCase):
    fixtures = ['initial_data.json']
    
    def test_vote(self):
        # Open the polls page
        self.driver.get('http://localhost:8000/polls/')
        # Get the link to the poll "How are you?"
        self.driver.save_screenshot('vote-page.png')
        poll = self.driver.find_element_by_link_text('How are you?')
        # Click on the link
        poll.click()
        # Load page
        time.sleep(2)
        # Get the available choices
        choices = self.driver.find_elements_by_name('choice')
        # Check that only two choices: "Fine." and "I'm great!"
        self.assertEquals(2, len(choices))
        # Select "Super cool"
        choices[1].click()
        # Submit the form
        choices[1].submit()
        # Get the poll results
        lis = self.driver.find_elements_by_tag_name('li')
        self.driver.save_screenshot('vote-result.png')
        # Check that results are displayed for each choices (two choices)
        self.assertEquals(2, len(lis))
        # Check that "Cool" has no votes
        self.assertEquals('Fine. -- 0 votes', lis[0].text)
        # Check that our vote for "I'm great!" was well stored
        self.assertEquals("I'm great! -- 1 vote", lis[1].text)

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
        password.send_keys('1234')
        # Submit the form
        password.submit()
        # Load page
        time.sleep(2)
        self.driver.save_screenshot('admin-welcome.png')
        # Check that welcomed
        self.assertTrue(self.driver.find_element_by_id('user-tools').text.startswith('Welcome'))
