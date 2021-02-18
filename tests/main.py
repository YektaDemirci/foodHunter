import unittest
from selenium import webdriver
import page
import os

#PATH = r"file:///Users/arshdeepkaurbal/Downloads/ece-651-project-search-bar-rahul 2/main.html"
#PATH = r"http://localhost:8000/main.html"
# when running the web app using python http server, use above PATH value

if __name__ == "__main__":
    unittest.main(verbosity=2)
# Tried to follow these docs:
# https://selenium-python.readthedocs.io/page-objects.html


# path_parent = os.path.dirname(os.getcwd())
# alternate implementation (os.getcwd was giving me 1 folder extra up the ladder)
path_parent = os.path.dirname(__file__)
path_parent = os.path.join(path_parent, os.pardir)
os.chdir(path_parent)

PATH = "file://"+os.getcwd()+"/main.html"

class FirstPageUI(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path= r'/Users/arshdeepkaurbal/Downloads/ece-651-project-search-bar-rahul 2/tests/geckodriver')
        self.driver.get(PATH)

    def test_search_bar(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_search_bar_empty()

    def test_empty_text(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_submit_empty()

    def test_one_input(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output()

    def test_multiple_options(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_options()

    def test_data_valid(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_valid()

    def test_input_spacing(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_spacing()

    def test_bad_input(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_err()

    @classmethod
    def tearDown(self):
        self.driver.close()


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