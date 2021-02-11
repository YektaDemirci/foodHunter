# Reference: https://stackoverflow.com/questions/16292634/always-allow-geolocation-in-firefox-using-selenium
import unittest
import os
import time
from selenium import webdriver


base_url = "http://localhost:8000/location/location.html"

# get the path of Firefox geckodriver
dir = os.path.dirname(__file__)
geckodriver_path = dir + "/geckodriver"

def setup(driver_options):
    # create a new Firefox session
    driver = webdriver.Firefox(executable_path=geckodriver_path, options=driver_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    # navigate to the application page
    driver.get(base_url)
    return driver


# Test 1: location access

class TestLocationAccess(unittest.TestCase):

    # Case 1: geolocation API not supported
    def test_case1(self):
        geoDisabled = webdriver.FirefoxOptions()
        geoDisabled.set_preference("geo.enabled", False)
        driver = setup(geoDisabled)
        # expect status error message
        statusMsg = driver.find_element_by_id("status").get_attribute("innerHTML")
        self.assertEqual(statusMsg, "Error: Your browser doesn't support geolocation.")
        # close the browser window
        driver.quit()

    # Case 2: geolocation supported but denied
    def test_case2(self):
        geoBlocked = webdriver.FirefoxOptions()
        geoBlocked.set_preference("geo.prompt.testing", True)
        geoBlocked.set_preference("geo.prompt.testing.allow", False)
        driver = setup(geoBlocked)
        # expect status error message
        statusMsg = driver.find_element_by_id("status").get_attribute("innerHTML")
        self.assertEqual(statusMsg, "Error: The Geolocation service failed.")
        # close the browser window
        driver.quit()

    # Case 3: geolocation supported, allowed and location mocked
    def test_case3(self):
        geoAllowed = webdriver.FirefoxOptions()
        geoAllowed.set_preference('geo.prompt.testing', True)
        geoAllowed.set_preference('geo.prompt.testing.allow', True)
        geoAllowed.set_preference('geo.provider.network.url',
            'data:application/json,{"location": {"lat": 43.6532, "lng": -79.3832}, "accuracy": 100.0}')
        driver = setup(geoAllowed)
        # expect no status error message
        statusMsg = driver.find_element_by_id("status").get_attribute("innerHTML")
        self.assertEqual(statusMsg, "")
        # expect 43°39'11.5"N 79°22'59.5"W on embedded map
        locationIframe = driver.find_element_by_id("location-map")
        time.sleep(5)
        driver.switch_to.frame(locationIframe)
        locationLatLon = driver.find_elements_by_class_name("place-name")[0].get_attribute("innerHTML")
        self.assertEqual(locationLatLon, '''43°39'11.5"N 79°22'59.5"W''')
        driver.switch_to.default_content()
        # close the browser window
        driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)