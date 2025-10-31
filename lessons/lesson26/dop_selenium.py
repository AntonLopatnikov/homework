from time import sleep
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    return chrome_driver


def test_new_tab(driver):
    driver.get("https://www.wildberries.ru/")
    driver.find_element(By.CSS_SELECTOR, '._close_1b9nk_55').click()
    driver.find_element(By.CSS_SELECTOR, '#diamondsMenu > div > ul > li.diamondsItem--bKv2p.j-avia').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.CSS_SELECTOR, '#__next > main > div:nth-child(1) > div > div:nth-child(1) > div.block-slider_heading__v8pB0')
    assert result.text == "Популярные направления"
    driver.close()
    driver.switch_to.window(tabs[0])
    select_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-card__wrapper'))
    )
    first_element = select_elements[0]
    yandex_link = first_element.find_element(By.CSS_SELECTOR, 'a.product-card__link')
    url = yandex_link.get_attribute('href')
    print(url)
    print(first_element.text)
    driver.get(url)
    result = driver.find_element(By.CSS_SELECTOR, '.mo-typography_variant_title3')
    assert result.text.strip(), "Заголовок отсутствует или пуст"
    print("Заголовок найден:", result.text)


def test_check_id(driver):
    driver.get("https://www.wildberries.ru/")
    check = driver.find_element(By.CSS_SELECTOR, '#diamondsMenu > div > ul > li.diamondsItem--bKv2p.j-avia')
    print(check.id)


# def test_iframe(driver):
#     driver.get("https://www.wildberries.ru/")
#     driver.find_element(By.CSS_SELECTOR, '._close_1b9nk_55').click()
#     iframe = driver.find_element(By.CSS_SELECTOR, '.banner-iframe')
#     driver.switch_to.frame(iframe)
#     banner = driver.find_element(By.XPATH, '//*[@name="banner_ab8c1441-4c34-4241-891a-731d1f5a0db7"]')

def test_dropdown(driver):
    driver.get("https://msk.ivanor.ru/")
    wheels_msk = driver.find_elements(By.CSS_SELECTOR, '.main-nav__link_wheel')
    alloy_wheels = driver.find_element(By.CSS_SELECTOR, 'body > div.site-wrapp > div.canvas > div > header > div.container > nav > ul > li.main-nav__item.main-nav__item_wheel > ul > li:nth-child(6) > a')
    ActionChains(driver).move_to_element(wheels_msk[0]).click(alloy_wheels).perform()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Литые диски'





