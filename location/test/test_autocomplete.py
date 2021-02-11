import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


base_url = "http://localhost:8000/location/location.html"
# get the path of Firefox geckodriver
dir = os.path.dirname(__file__)
geckodriver_path = dir + "/geckodriver"

def enter_text_to_get_first_dropdown_item(driver, location_input, input_text):
    # enter text in location-input textbox
    location_input.clear()
    location_input.send_keys(input_text)
    time.sleep(2)
    # get a list of dropdown items
    dropdownItems = driver.find_elements_by_class_name("pac-container")[0] \
        .find_elements_by_class_name("pac-item")
    firstItem = dropdownItems[0]
    placeName = firstItem.find_element_by_class_name("pac-item-query").text
    placeAddress = firstItem.text.replace(placeName,"")
    return (placeName, placeAddress)

def click_first_dropdown_item_to_get_map(driver, location_input, location_iframe):
    # click 1st item
    location_input.send_keys(Keys.DOWN)
    location_input.send_keys(Keys.RETURN)
    # expect location updated on embedded map
    time.sleep(5)
    driver.switch_to.frame(location_iframe)
    placeName = driver.find_elements_by_class_name("place-name")[0] \
        .get_attribute("innerHTML")
    placeAddress = driver.find_elements_by_class_name("address")[0] \
        .get_attribute("innerHTML")
    driver.switch_to.default_content()
    return (placeName, placeAddress)


# Test 2: address autocomplete

class TestAutocomplete(unittest.TestCase):
    
    def setUp(self):
        # geolocation supported but denied
        geoBlocked = webdriver.FirefoxOptions()
        geoBlocked.set_preference("geo.prompt.testing", True)
        geoBlocked.set_preference("geo.prompt.testing.allow", False)
        # create a new Firefox session
        self.driver = webdriver.Firefox( \
            executable_path=geckodriver_path, options=geoBlocked)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        # navigate to the application page
        self.driver.get(base_url)
        # address autocomplete
        self.location_input = self.driver.find_element_by_id("location-input")
        # embedded map
        self.location_iframe = self.driver.find_element_by_id("location-map")

    # Case 1: "University of Waterloo"
    def test_case1(self):
        firstItemName, _ = enter_text_to_get_first_dropdown_item(self.driver, \
            self.location_input, "University of Waterloo")
        self.assertEqual(firstItemName, "University of Waterloo")
        placeName, placeAddress = click_first_dropdown_item_to_get_map(self.driver, \
            self.location_input, self.location_iframe)
        self.assertEqual(placeName, "Engineering 5")
        self.assertEqual(placeAddress, "200 University Ave W, Waterloo, ON N2L 3E9")

    # Case 2: "200 University Ave W, Waterloo, ON"
    def test_case2(self):
        firstItemName, firstItemAddress = enter_text_to_get_first_dropdown_item(self.driver, \
            self.location_input, "200 University Ave W, Waterloo, ON")
        self.assertEqual(firstItemName, "200 University Ave W")
        self.assertEqual(firstItemAddress, "Waterloo, Ontario, Canada")
        placeName, placeAddress = click_first_dropdown_item_to_get_map(self.driver, \
            self.location_input, self.location_iframe)
        self.assertEqual(placeName, "Engineering 5")
        self.assertEqual(placeAddress, "200 University Ave W, Waterloo, ON N2L 3E9")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)