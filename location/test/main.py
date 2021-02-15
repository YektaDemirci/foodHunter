import unittest
import time
from selenium import webdriver
import page


class TestLocation(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox( \
            executable_path=page.geckodriver_path, \
            options=page.getDriverGeoOption("denied"))
        self.driver.get(page.base_url)

    # driver geo option: access disabled
    def test_geolocation_access_disabled(self):
        mainPage = page.MainPage(self.driver)
        mainPage.switch_driver("disabled")
        self.assertEqual(mainPage.get_status(), \
            "Error: Your browser doesn't support geolocation.")
        mainPage.close_driver()

    # default driver geo option: access denied
    def test_geolocation_access_denied(self):
        mainPage = page.MainPage(self.driver)
        self.assertEqual(mainPage.get_status(), \
            "Error: The Geolocation service failed.")

    # driver geo option: access allowed
    def test_geolocation_access_allowed(self):
        mainPage = page.MainPage(self.driver)
        mainPage.switch_driver("allowed")
        self.assertEqual(mainPage.get_status(), "")
        time.sleep(5)
        place_name, _ = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(place_name, '''43°39'11.5"N 79°22'59.5"W''')
        mainPage.close_driver()

    def test_autocomplete_with_place_name(self):
        mainPage = page.MainPage(self.driver)
        mainPage.location_search_text_element = "University of Waterloo"
        time.sleep(2)
        first_item_name, _ = mainPage.get_first_dropdown_item_name_and_address()
        self.assertEqual(first_item_name, "University of Waterloo")
        mainPage.click_first_dropdown_item()
        time.sleep(5)
        place_name, place_address = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(place_name, "Engineering 5")
        self.assertEqual(place_address, "200 University Ave W, Waterloo, ON N2L 3E9")
    
    def test_autocomplete_with_place_address(self):
        mainPage = page.MainPage(self.driver)
        mainPage.location_search_text_element = "200 University Ave W, Waterloo, ON"
        time.sleep(2)
        first_item_name, first_item_address = mainPage.get_first_dropdown_item_name_and_address()
        self.assertEqual(first_item_name, "200 University Ave W")
        self.assertEqual(first_item_address, "Waterloo, Ontario, Canada")
        mainPage.click_first_dropdown_item()
        time.sleep(5)
        place_name, place_address = mainPage.get_location_map_place_name_and_address()
        self.assertEqual(place_name, "Engineering 5")
        self.assertEqual(place_address, "200 University Ave W, Waterloo, ON N2L 3E9")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)