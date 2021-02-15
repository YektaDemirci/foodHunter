import unittest
import time
from selenium import webdriver
import page


def getDriver(driver_geo_option_arg):
    driver = webdriver.Firefox( \
        executable_path=page.geckodriver_path, \
        options=page.getDriverGeoOption(driver_geo_option_arg))
    driver.get(page.base_url)
    driver.implicitly_wait(3)
    return driver


class TestLocation(unittest.TestCase):
    
    def setUp(self):
        self.driver = getDriver("denied")
    
    def test_1_geolocation_access(self):
        # case 1: access denied
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(1)
        self.assertEqual(mainPage.get_status(), \
            "Error: The Geolocation service failed.")
        self.driver.quit()
        time.sleep(3)
        # case 2: access allowed
        self.driver = getDriver("allowed")
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(1)
        self.assertEqual(mainPage.get_status(), "")
        time.sleep(5)
        placeName, _ = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(placeName, '''43°39'11.5"N 79°22'59.5"W''')
        self.driver.quit()
        time.sleep(3)
        # case 3: access disallowed
        self.driver = getDriver("disabled")
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(1)
        self.assertEqual(mainPage.get_status(), \
            "Error: Your browser doesn't support geolocation.")
    
    def test_2_autocomplete_with_place_address(self):
        mainPage = page.MainPage(self.driver)
        mainPage.location_search_text_element = "200 University Ave W, Waterloo, ON"
        time.sleep(3)
        firstItemName, firstItemAddress = mainPage.get_first_dropdown_item_name_and_address()
        self.assertEqual(firstItemName, "200 University Ave W")
        self.assertEqual(firstItemAddress, "Waterloo, Ontario, Canada")
        mainPage.click_first_dropdown_item()
        time.sleep(5)
        _, placeAddress = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(placeAddress, "200 University Ave W, Waterloo, ON N2L 3E9")

    def test_3_autocomplete_with_postal_code(self):
        mainPage = page.MainPage(self.driver)
        mainPage.location_search_text_element = "N2L 3E9"
        time.sleep(3)
        firstItemName, firstItemAddress = mainPage.get_first_dropdown_item_name_and_address()
        self.assertEqual(firstItemName, "N2L 3E9")
        self.assertEqual(firstItemAddress, "Waterloo, ON, Canada")
        mainPage.click_first_dropdown_item()
        time.sleep(5)
        placeName, placeAddress = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(placeName, "Waterloo, ON N2L 3E9")
        self.assertEqual(placeAddress, "Waterloo, ON")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)