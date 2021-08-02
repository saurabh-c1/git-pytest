import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_url = "https://www.w3schools.com/html/html_tables.asp"


class WebTableTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            driver = webdriver.Chrome("chromedriver.exe")
            driver.get(test_url)
            driver.maximize_window()
        except:
            print("Failed")

    def test_getrows(driver):
        try:
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))

            num_rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
            print("Rows in table are " + repr(num_rows))
        except:
            print("Failed")

    def test_getcols(driver):
        try:
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))
            num_cols = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/th"))
            print("Columns in table are " + repr(num_cols))
        except:
            print("Failed")

    @classmethod
    def tearDownClass(cls, driver):
        try:
            driver.close()
            driver.quit()
        except:
            print("Failed")


if __name__ == "__main__":
    unittest.main()
