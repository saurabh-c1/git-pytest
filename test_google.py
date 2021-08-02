from selenium import webdriver
from selenium.webdriver import ActionChains


def test_google():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://google.com")
    assert driver.title == "Google"
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://facebook.com")
    assert driver.title == "Facebook - लॉग इन किंवा साइन अप"
    driver.quit()


def test_instagram():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://instagram.com")
    assert driver.title == "Instagram"
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://gmail.com")
    assert driver.title == "Gmail"
    driver.quit()


def test_rediff():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.rediff.com/")
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()

