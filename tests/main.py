import unittest
from BackendTest import FirstPageUI, LocationPageUI, LocationPageUI_GeoDenied, LocationPageUI_GeoDisabled
from FrontendTest import FooterUI
from DatabaseTest import DBTest

# get all tests from backend and frontend
main_test = unittest.TestLoader().loadTestsFromTestCase(FirstPageUI)
location_test = unittest.TestLoader().loadTestsFromTestCase(LocationPageUI)
location_test_geo_denied = unittest.TestLoader().loadTestsFromTestCase(LocationPageUI_GeoDenied)
location_test_geo_disabled = unittest.TestLoader().loadTestsFromTestCase(LocationPageUI_GeoDisabled)
footer_test = unittest.TestLoader().loadTestsFromTestCase(FooterUI)
db_test = unittest.TestLoader().loadTestsFromTestCase(DBTest)


# create a test suite
test_suite = unittest.TestSuite([main_test, location_test, location_test_geo_denied, location_test_geo_disabled, footer_test, db_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
