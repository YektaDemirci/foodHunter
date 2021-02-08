import unittest
from selenium import webdriver
import page

PATH = r"file:///Users/arshdeepkaurbal/Downloads/ece-651-project-search-bar-rahul 2/main.html"
#PATH = r"http://localhost:8000/main.html"
# when running the web app using python http server, use above PATH value

class FirstPageUI(unittest.TestCase):

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

    def test_input_spacing(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_spacing()

    def test_bad_input(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_err()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
