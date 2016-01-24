# -*-coding: UTF-8 -*-

import unittest
from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_valida_campos(self):
        self.driver.get("http://localhost:8000/admin")

        # bind
        field_username = self.driver.find_element_by_id("id_username")
        field_password = self.driver.find_element_by_id("id_password")
        btn_login = self.driver.find_element_by_xpath("//input[@value='Log in']")

        # set
        field_username.send_keys("")
        field_password.send_keys("")
        btn_login.click()
        assert "This field is required." in self.driver.find_element_by_css_selector("form").text

        # bind
        field_username = self.driver.find_element_by_id("id_username")
        field_password = self.driver.find_element_by_id("id_password")
        btn_login = self.driver.find_element_by_xpath("//input[@value='Log in']")

        # set
        field_username.send_keys("admin")
        field_password.send_keys("")
        btn_login.click()
        assert "This field is required." in self.driver.find_element_by_css_selector("form").text

        # bind
        field_username = self.driver.find_element_by_id("id_username")
        field_password = self.driver.find_element_by_id("id_password")
        btn_login = self.driver.find_element_by_xpath("//input[@value='Log in']")

        # set
        field_username.clear()
        field_password.send_keys("admin")
        btn_login.click()
        assert "This field is required." in self.driver.find_element_by_css_selector("form").text

    def test_login(self):
        # User
        user = "admin"
        pwd = "admin"

        self.driver.get("http://localhost:8000/admin")
        field_username = self.driver.find_element_by_id("id_username")
        field_password = self.driver.find_element_by_id("id_password")
        btn_login = self.driver.find_element_by_xpath("//input[@value='Log in']")

        # Auth
        field_username.send_keys(user)
        field_password.send_keys(pwd)
        btn_login.click()

        # Asserts
        # Validation
        user_logged = self.driver.find_element_by_xpath("//div[@id='user-tools']/strong").text
        assert "ADMIN" == user_logged
        assert "Site administration | Django site admin" == self.driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()