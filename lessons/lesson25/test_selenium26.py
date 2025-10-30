import pytest
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_id_name(driver):
    input_data = "cat"
    driver.get("https://www.google.com/?hl=ru")
    # text_string = driver.find_element(By.ID, "APjFqb")
    text_string = driver.find_element(By.NAME, "q")
    text_string.send_keys(input_data)
    # text_string.submit()
    text_string.send_keys(Keys.ENTER)
    assert text_string.get_attribute("value") == input_data


def test_css_selector(driver):
    driver.get("https://www.google.com/")
    class_string = driver.find_element(By.CSS_SELECTOR, '[data-pid="2"]')
    print(class_string.get_attribute("innerText"))
    assert class_string.get_attribute("innerText") == 'Картинки'
    assert class_string.get_attribute('aria-label') == 'Поиск картинок '
    class_string.click()
    assert "Картинки Google" in driver.title




def test_xpath(driver):
    driver.get("https://www.google.com/")
    class_string = driver.find_element(By.XPATH, '//*[@data-pid="23"]')
    assert class_string.get_attribute("innerText") == 'Почта'
    print(class_string.get_attribute("innerText"))
    class_string.click()








