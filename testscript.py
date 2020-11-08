import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://192.168.10.168:3000/")
        #self.assertIn("192.168.10.168:3000", driver.title)
        elem = driver.find_element_by_tag_name("body")
        assert "Helloe World!", elem.text
        #elem.send_keys(Keys.RETURN)
        #assert "Hello World!" not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
