import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import warnings
import page


def getDriver(driver_geo_option_arg="allowed"):
    path_parent = os.path.dirname(__file__)
    path_parent = os.path.join(path_parent, os.pardir)
    os.chdir(path_parent)

    PATH = "file://"+os.getcwd()+"/main.html"

    driver = webdriver.Firefox( \
        options=getDriverOption(driver_geo_option_arg), \
        executable_path='tests/geckodriver', \
        service_log_path='/dev/null')
    driver.get(PATH)
    driver.implicitly_wait(3)
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    return driver


class FirstPageUI(unittest.TestCase):
    @classmethod
    def setUp(self):
        # Geckodriver in tests folder doesnt work for me (I think its computer architecture specific)
        '''
        Might be just due to different executable_path for geckodriver.
        Should be solved now because test/geckodriver is not in gitignore.
        '''
        # self.driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver", service_log_path = '/dev/null')
        self.driver = getDriver()

    def test_empty_input(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_input_empty()

    def test_one_ingredient_input(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.has_output_for_one_ingredient()

    def test_multiple_ingredients_input(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.has_output_for_multiple_ingredients()
    
    def test_different_inputs(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.has_output_for_different_inputs()
    
    def test_input_with_spacing(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.has_output_for_input_with_spacing()

    def test_bad_input(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.has_no_output_for_bad_input()

    def test_output_matching_input_ingredients(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_with_matching_ingredients()
    
    def test_output_sorted_by_distance(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_output_sorted_by_distance()

    def test_selection_present(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_div_present()

    def test_selection_deleted(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_div_deleted()

    def test_clear_all(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_all_div_deleted()

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class LocationPageUI(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = getDriver()

    def test_geolocation_access_allowed(self):
        mainPage = page.LocationModalPage(self.driver)
        assert mainPage.is_geolocation_access_allowed()

    def test_location_search_bar_with_address(self):
        mainPage = page.LocationModalPage(self.driver)
        assert mainPage.is_location_output_valid('address')

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class LocationPageUI_GeoDenied(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = getDriver("denied")

    def test_geolocation_access_denied(self):
        mainPage = page.LocationModalPage(self.driver)
        assert mainPage.is_geolocation_access_denied()

    def test_location_search_bar_with_postal_code(self):
        mainPage = page.LocationModalPage(self.driver)
        assert mainPage.is_location_output_valid('postal_code')

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class LocationPageUI_GeoDisabled(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = getDriver("disabled")

    def test_geolocation_access_disabled(self):
        mainPage = page.LocationModalPage(self.driver)
        assert mainPage.is_geolocation_access_disabled()
    
    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


def getDriverOption(argument):
    option = Options()
    option.add_argument('-headless')
    if argument == "disabled":
        option.set_preference("geo.enabled", False)
    elif argument == "denied":
        option.set_preference("geo.prompt.testing", True)
        option.set_preference("geo.prompt.testing.allow", False)
    elif argument == "allowed":
        option.set_preference('geo.prompt.testing', True)
        option.set_preference('geo.prompt.testing.allow', True)
        # set mock geolocation to University of Waterloo Station
        option.set_preference('geo.provider.network.url',
            'data:application/json,{"location": {"lat": 43.4733, "lng": -80.5410}, "accuracy": 100.0}')
    return option


if __name__ == "__main__":
    unittest.main(verbosity=2)
