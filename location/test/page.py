import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locator import *
from element import BasePageElement


# test page url
base_url = "http://localhost:8000/location/location.html"
# path of Firefox geckodriver
geckodriver_path = os.path.dirname(__file__) + "/geckodriver"

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
        # set mock geolocation to Toronto
        geoOption.set_preference('geo.provider.network.url',
            'data:application/json,{"location": {"lat": 43.6532, "lng": -79.3832}, "accuracy": 100.0}')
    return geoOption


class LocationSearchTextElement(BasePageElement):
    def __init__(self):
        self.locator = MainPageLocators.LOCATION_INPUT


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    location_search_text_element = LocationSearchTextElement()

    def switch_driver(self, driver_geo_option_arg):
        #self.driver_original = self.driver
        self.driver = webdriver.Firefox( \
            executable_path=geckodriver_path, \
            options=getDriverGeoOption(driver_geo_option_arg))
        self.driver.get(base_url)

    def close_driver(self):
        self.driver.quit()
        #self.driver = self.driver_original
        #delattr(MainPage, 'driver_original')

    def get_status(self):
        return self.driver.find_element(*MainPageLocators.STATUS_DIV).get_attribute("innerHTML")

    def get_location_map_place_name_and_address(self):
        location_iframe = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME)
        self.driver.switch_to.frame(location_iframe)
        placeName = self.driver.find_elements_by_class_name("place-name")[0] \
            .get_attribute("innerHTML")
        placeAddress = self.driver.find_elements_by_class_name("address")[0] \
            .get_attribute("innerHTML")
        self.driver.switch_to.default_content()
        return (placeName, placeAddress)

    def get_first_dropdown_item_name_and_address(self):
        dropdownItems = self.driver.find_elements_by_class_name("pac-container")[0] \
            .find_elements_by_class_name("pac-item")
        firstItem = dropdownItems[0]
        placeName = firstItem.find_element_by_class_name("pac-item-query").text
        placeAddress = firstItem.text.replace(placeName,"")
        return (placeName, placeAddress)

    def click_first_dropdown_item(self):
        location_input = self.driver.find_element(*MainPageLocators.LOCATION_INPUT)
        location_input.send_keys(Keys.DOWN)
        location_input.send_keys(Keys.RETURN)