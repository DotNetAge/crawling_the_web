from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"kw"))
    )
finally:
    print element
    driver.quit()