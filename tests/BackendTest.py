import unittest
import time
import os
from selenium import webdriver
import warnings
import page

#PATH = r"file:///Users/arshdeepkaurbal/Downloads/ece-651-project-search-bar-rahul 2/main.html"
#PATH = r"http://localhost:8000/main.html"
# when running the web app using python http server, use above PATH value

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
        #self.driver = webdriver.Firefox(executable_path=r'tests/geckodriver')
        #self.driver.get(PATH)
        self.driver = getDriver("allowed")

    def test_search_bar(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_search_bar_empty()

    def test_empty_text(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_submit_empty()

    def test_one_input(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(5)
        assert mainPage.is_output()

    def test_multiple_options(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(5)
        assert mainPage.is_output_options()

    def test_data_valid(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(5)
        assert mainPage.is_output_valid()

    def test_input_spacing(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(5)
        assert mainPage.is_output_spacing()

    def test_bad_input(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(5)
        assert mainPage.is_output_err()

    def test_geolocation_access_allowed(self):
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(1)
        self.assertEqual(mainPage.get_location_status(), "")
        time.sleep(5)
        placeName, _ = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(placeName, '''43°28'23.9"N 80°32'27.6"W''')
    
    def test_location_search_bar_with_place_address(self):
        mainPage = page.MainPage(self.driver)
        mainPage.location_search_bar_element = "200 University Ave W, Waterloo, ON"
        time.sleep(3)
        firstItemName, firstItemAddress = mainPage.get_location_first_dropdown_item_name_and_address()
        self.assertEqual(firstItemName, "200 University Ave W")
        self.assertEqual(firstItemAddress, "Waterloo, Ontario, Canada")
        mainPage.click_location_first_dropdown_item()
        time.sleep(5)
        placeName, _ = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(placeName, "Engineering 5")

    @classmethod
    def tearDown(self):
        self.driver.close()


class FirstPageUI_GeoDenied(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = getDriver("denied")

    def test_geolocation_access_denied(self):
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(1)
        self.assertEqual(mainPage.get_location_status(), \
            "Error: The Geolocation service failed.")
    
    def test_location_search_bar_with_postal_code(self):
        mainPage = page.MainPage(self.driver)
        mainPage.location_search_bar_element = "N2L 3E9"
        time.sleep(3)
        firstItemName, firstItemAddress = mainPage.get_location_first_dropdown_item_name_and_address()
        self.assertEqual(firstItemName, "N2L 3E9")
        self.assertEqual(firstItemAddress, "Waterloo, ON, Canada")
        mainPage.click_location_first_dropdown_item()
        time.sleep(5)
        placeName, _ = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(placeName, "Waterloo, ON N2L 3E9")

    @classmethod
    def tearDown(self):
        self.driver.close()


class FirstPageUI_GeoDisabled(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = getDriver("disabled")

    def test_geolocation_access_disabled(self):
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(1)
        self.assertEqual(mainPage.get_location_status(), \
            "Error: Your browser doesn't support geolocation.")
    
    @classmethod
    def tearDown(self):
        self.driver.close()


def getDriver(driver_geo_option_arg):
    driver = webdriver.Firefox( \
        executable_path=r'tests/geckodriver', \
        options=getDriverGeoOption(driver_geo_option_arg))
    driver.get(PATH)
    driver.implicitly_wait(3)
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    return driver

def getDriverGeoOption(argument):
    geoOption = webdriver.FirefoxOptions()
    if argument == "disabled":
        geoOption.set_preference("geo.enabled", False)
    elif argument == "denied":
        geoOption.set_preference("geo.prompt.testing", True)
        geoOption.set_preference("geo.prompt.testing.allow", False)
    elif argument == "allowed":
        geoOption.set_preference('geo.prompt.testing', True)
        geoOption.set_preference('geo.prompt.testing.allow', True)
        # set mock geolocation to University of Waterloo Station
        geoOption.set_preference('geo.provider.network.url',
            'data:application/json,{"location": {"lat": 43.4733, "lng": -80.5410}, "accuracy": 100.0}')
    return geoOption

if __name__ == "__main__":
    unittest.main(verbosity=2)