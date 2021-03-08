import unittest
from selenium import webdriver
import page
import os
from selenium.webdriver.firefox.options import Options

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

options = Options()
options.headless = True

class FirstPageUI(unittest.TestCase):
    @classmethod
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=r'tests/geckodriver', service_log_path = os.path.devnull)
        self.driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver", service_log_path = '/dev/null')
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
        self.driver.quit()