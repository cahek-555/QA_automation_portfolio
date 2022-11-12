import os
import time
import unittest

from selenium import webdriver

from pages.add_player_page import AddPlayer
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestCreatePlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_create_player(self):
        self.user_login = LoginPage(self.driver)
        self.user_login.type_in_email('user01@getnada.com')
        self.user_login.type_in_password('Test-1234')
        self.user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        time.sleep(7)
        dashboard_page.check_title_of_page()
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayer(self.driver)
        add_player.type_in_name("Lera")
        add_player.type_in_surname("Pop")
        add_player.type_in_left_leg()
        add_player.type_in_age("20.05.1992")
        add_player.type_in_position("testing")
        add_player.click_on_the_submit_button()
        time.sleep(7)

    @classmethod
    def tearDown(self):
        self.driver.quit()
