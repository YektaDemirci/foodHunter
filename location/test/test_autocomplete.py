import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "http://localhost:8000/location/location.html"

# get the path of Firefox geckodriver
dir = os.path.dirname(__file__)
geckodriver_path = dir + "/geckodriver"

# Test 2: address autocomplete

# geolocation supported but denied
geoBlocked = webdriver.FirefoxOptions()
geoBlocked.set_preference("geo.prompt.testing", True)
geoBlocked.set_preference("geo.prompt.testing.allow", False)
# create a new Firefox session
driver = webdriver.Firefox(executable_path=geckodriver_path, options=geoBlocked)
driver.implicitly_wait(5)
driver.maximize_window()
# navigate to the application home page
driver.get(base_url)

# address autocomplete
address_input = driver.find_element_by_id("location-input")
# embedded map
iframe = driver.find_element_by_id("location-map")

# Case 1: "University of Waterloo"
address_input.send_keys("University of Waterloo")
time.sleep(2)
dropdown_list_items = driver.find_elements_by_class_name("pac-container")[0].find_elements_by_class_name("pac-item")
print("Case 1:")
for item in dropdown_list_items:
    print(item.text)
# click 1st item
address_input.send_keys(Keys.DOWN)
address_input.send_keys(Keys.RETURN)
# expect matching name on embedded map
time.sleep(5)
driver.switch_to.frame(iframe)
placeName = driver.find_elements_by_class_name("place-name")[0].get_attribute("innerHTML")
placeAddress = driver.find_elements_by_class_name("address")[0].get_attribute("innerHTML")
print("place name: "+placeName)
print("place address: "+placeAddress)
driver.switch_to.default_content()

# Case 2: "200 University Ave W, Waterloo, ON"
address_input.clear()
address_input.send_keys("200 University Ave W, Waterloo, ON")
time.sleep(2)
dropdown_list_items = driver.find_elements_by_class_name("pac-container")[0].find_elements_by_class_name("pac-item")
print("Case 2:")
for item in dropdown_list_items:
    # 2 matching results
    print(item.text)
# click 1st item
address_input.send_keys(Keys.DOWN)
address_input.send_keys(Keys.RETURN)
# expect matching name on embedded map
time.sleep(5)
driver.switch_to.frame(iframe)
placeName = driver.find_elements_by_class_name("place-name")[0].get_attribute("innerHTML")
placeAddress = driver.find_elements_by_class_name("address")[0].get_attribute("innerHTML")
print("place name: "+placeName)
print("place address: "+placeAddress)
driver.switch_to.default_content()

# close the browser window
driver.quit()