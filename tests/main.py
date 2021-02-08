# Tried to follow these docs:
# https://selenium-python.readthedocs.io/page-objects.html

import unittest
from selenium import webdriver
import page

PATH = "file:///home/andy/Documents/ECE651/ece-651-project/main.html"

class FooterUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(PATH)

    def test_footerStep1(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_footer_step1_highlighted(), "\nInitial styling of footer is incorrect"

    def test_footerStep2(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_footer_step2_highlighted(), "\nStyling for second step is incorrect"

    def test_footerStep3(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_footer_step3_highlighted(), "\nStyling for final step is incorrect"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
