import unittest
from BackendTest import FirstPageUI, FirstPageUI_GeoDenied, FirstPageUI_GeoDisabled
from FrontendTest import FooterUI
from DatabaseTest import DBTest

# get all tests from backend and frontend
search_text = unittest.TestLoader().loadTestsFromTestCase(FirstPageUI)
search_text_geo_denied = unittest.TestLoader().loadTestsFromTestCase(FirstPageUI_GeoDenied)
search_text_geo_disabled = unittest.TestLoader().loadTestsFromTestCase(FirstPageUI_GeoDisabled)
footer_test = unittest.TestLoader().loadTestsFromTestCase(FooterUI)
db_test = unittest.TestLoader().loadTestsFromTestCase(DBTest)


# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([footer_test,search_text, search_text_geo_denied, search_text_geo_disabled, db_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
