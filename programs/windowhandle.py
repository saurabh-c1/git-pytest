import time

from selenium import webdriver

driver = webdriver.Chrome("../chromedriver.exe")
driver.maximize_window()
driver.get("https://courses.letskodeit.com/practice")

driver.find_element_by_id("openwindow").click()
parent = driver.current_window_handle
handles = driver.window_handles
size = len(handles)

for x in range(size):
    if handles[x] != parent:
        driver.switch_to.window(handles[x])
        time.sleep(2)
        print(driver.title)
        driver.close()
        break
driver.switch_to.window(parent)
driver.find_element_by_id("openwindow").click()
