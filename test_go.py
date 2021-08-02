import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    print("\n------------------SETUP-----------------")
    if request.param == "chrome":
        driver = webdriver.Chrome("chromedriver.exe")
    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    print("\n------------------TEARDOWN-----------------")
    driver.close()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestGoogle(BaseTest):
    def test_google_title(self):
        self.driver.get("http://google.com")
        assert self.driver.title == "Google"

    def test_google_url(self):
        self.driver.get("http://google.com")
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"
