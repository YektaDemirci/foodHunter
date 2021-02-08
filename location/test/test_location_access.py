# Reference: https://stackoverflow.com/questions/16292634/always-allow-geolocation-in-firefox-using-selenium

import os
import time
from selenium import webdriver

base_url = "http://localhost:8000/location/location.html"

# get the path of Firefox geckodriver
dir = os.path.dirname(__file__)
geckodriver_path = dir + "/geckodriver"

# Test 1: location access

# Case 1: geolocation API not supported
geoDisabled = webdriver.FirefoxOptions()
geoDisabled.set_preference("geo.enabled", False)
# create a new Firefox session
driver = webdriver.Firefox(executable_path=geckodriver_path, options=geoDisabled)
driver.implicitly_wait(5)
driver.maximize_window()
# navigate to the application home page
driver.get(base_url)
# expect status error message
status_msg = driver.find_element_by_id("status").get_attribute("innerHTML")
print("Case 1:")
print("status: "+status_msg)
# close the browser window
driver.quit()

# Case 2: geolocation supported but denied
geoBlocked = webdriver.FirefoxOptions()
geoBlocked.set_preference("geo.prompt.testing", True)
geoBlocked.set_preference("geo.prompt.testing.allow", False)
# create a new Firefox session
driver = webdriver.Firefox(executable_path=geckodriver_path, options=geoBlocked)
driver.implicitly_wait(5)
driver.maximize_window()
# navigate to the application home page
driver.get(base_url)
# expect status error message
status_msg = driver.find_element_by_id("status").get_attribute("innerHTML")
print("Case 2:")
print("status: "+status_msg)
# close the browser window
driver.quit()

# Case 3: geolocation supported, allowed and location mocked
geoAllowed = webdriver.FirefoxOptions()
geoAllowed.set_preference('geo.prompt.testing', True)
geoAllowed.set_preference('geo.prompt.testing.allow', True)
geoAllowed.set_preference('geo.provider.network.url',
    'data:application/json,{"location": {"lat": 43.6532, "lng": -79.3832}, "accuracy": 100.0}')
driver = webdriver.Firefox(executable_path=geckodriver_path, options=geoAllowed)
driver.implicitly_wait(5)
driver.maximize_window()
# navigate to the application home page
driver.get(base_url)
# expect status error message
status_msg = driver.find_element_by_id("status").get_attribute("innerHTML")
print("Case 3:")
print("status: "+status_msg)
# expect 43°39'11.5"N 79°22'59.5"W on embedded map
iframe = driver.find_element_by_id("location-map")
time.sleep(5)
driver.switch_to.frame(iframe)
lat_lon = driver.find_elements_by_class_name("place-name")[0].get_attribute("innerHTML")
print("lat & lon: "+lat_lon)
driver.switch_to.default_content()
# close the browser window
driver.quit()