from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOCATION_INPUT = (By.ID, "location-input")
    LOCATION_IFRAME = (By.ID, "location-map")
    STATUS_DIV = (By.ID, "status")
    # class name assigned by Google API
    LOCATION_DROPDOWN = (By.CLASS_NAME, "pac-container")
    LOCATION_DROPDOWN_ITEM = (By.CLASS_NAME, "pac-item")
    LOCATION_DROPDOWN_ITEM_PLACE_INFO = (By.CLASS_NAME, "pac-item-query")
    LOCATION_IFRAME_PLACE_NAME = (By.CLASS_NAME, "place-name")
    LOCATION_IFRAME_PLACE_ADDRESS = (By.CLASS_NAME, "address")