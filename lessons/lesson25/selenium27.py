from time import sleep

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

from lessons.lesson25.lesson_24 import test_same_elements


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    return chrome_driver

def test_clear(driver):
    input_data = "cat"
    driver.get("https://www.google.com/?hl=ru")
    # text_string = driver.find_element(By.ID, "APjFqb")
    text_string = driver.find_element(By.NAME, "q")
    text_string.send_keys(input_data)
    # text_string.submit()
    value = (text_string.get_attribute("value"))
    for _ in range(len(value)):
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.is_displayed()



def test_inabled_select(driver):
    driver.get("https://www.google.com/")
    button = driver.find_element(By.CSS_SELECTOR, '.gNO89b')
    print(button.is_enabled())
    selects = driver.find_element(By.CSS_SELECTOR, '[class="RNmpXc"]')
    # dropdown = Select(selects)
    # dropdown.select_by_value('Мне повезёт!')
    print(selects.is_enabled())

def test_adding_cart(driver):
    driver.get("https://www.wildberries.ru/catalog/217159439/detail.aspx?targetUrl=EX")
    choose_clothes = driver.find_element(By.CSS_SELECTOR, '[data-nm-id="235508589"]')
    choose_clothes.click()
    size_selection = driver.find_element(By.CSS_SELECTOR, '.sizesListSize--NUoNC')
    size_selection.click()
    basket = driver.find_element(By.CSS_SELECTOR, '.orderFixedContainer--l1ZSv')
    basket.click()
    click_basket = driver.find_element(By.CSS_SELECTOR, '.navbar-pc__icon--basket')
    click_basket.click()
    check_basket = driver.find_element(By.CSS_SELECTOR, '.good-info__good-name')
    assert click_basket.text == '1'
    assert check_basket.text == 'Костюм муслин летний рубашка с шортами черный оверсайз'
    clear_basket = driver.find_element(By.CSS_SELECTOR, '.btn__del.j-basket-item-del')
    clear_basket.click()
    WebDriverWait(driver, 6).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, '.navbar-pc__notify')))
    assert len(driver.find_elements(By.CSS_SELECTOR, '.navbar-pc__notify')) == 0
    driver.add_cookie({'name': 'test', 'value': 'testvalue'})
    print(driver.get_cookies())
    # driver.delete_all_cookies()


def test_elements(driver):
    driver.get("https://www.wildberries.ru/")
    select_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-card__wrapper'))
    )
    first_element = select_elements[0]
    link = first_element.find_element(By.CSS_SELECTOR, 'a.product-card__link')
    url = link.get_attribute('href')
    print(first_element.text)
    print(url)


def test_elements2(driver):
    driver.get("https://www.wildberries.ru/")
    select_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-card__wrapper'))
    )
    for cards in select_elements:
        print(cards.find_element(By.CSS_SELECTOR, '.price__lower-price').text)
        # print(select_elements[0].find_element(By.CSS_SELECTOR, '.price__lower-price').text)























