import unittest
from BackendTest import FirstPageUI
from FrontendTest import FooterUI

# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(FirstPageUI)
footer_test = unittest.TestLoader().loadTestsFromTestCase(FooterUI)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([footer_test, search_text])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)