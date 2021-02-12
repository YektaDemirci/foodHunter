# Tried to follow these docs:
# https://selenium-python.readthedocs.io/page-objects.html

import unittest
from selenium import webdriver
import page
import os

# path_parent = os.path.dirname(os.getcwd())
# alternate implementation (os.getcwd was giving me 1 folder extra up the ladder)
path_parent = os.path.dirname(__file__)
path_parent = os.path.join(path_parent, os.pardir)
os.chdir(path_parent)

PATH = "file://"+os.getcwd()+"/main.html"

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

    def test_boxStep1(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step1_highlighted(), "\nStyling for box 1st step is incorrect"

    def test_boxStep2(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step2_highlighted(), "\nStyling for box 2nd step is incorrect"
    
    def test_boxStep3(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step3_highlighted(), "\nStyling for box 3th step is incorrect"
    
    def test_boxStep2re(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step2_rehighlighted(), "\nStyling for box 2nd re-step is incorrect"
    
    def test_boxStep1re(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step1_rehighlighted(), "\nStyling for box 1st re-step is incorrect"


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
