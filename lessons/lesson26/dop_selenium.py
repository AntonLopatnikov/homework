
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
    close_banner = driver.find_element(By.CSS_SELECTOR, '._close_1b9nk_55')
    close_banner.click()
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
    wheels_msk = driver.find_element(By.CSS_SELECTOR, '.main-nav__link_wheel')
    alloy_wheels = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/header/div[3]/nav/ul/li[2]/ul/li[6]/a')
    actions = ActionChains(driver)
    actions.move_to_element(wheels_msk)
    actions.click(alloy_wheels)
    actions.perform()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Литые диски'

def test_scroll(driver):
    driver.get("https://www.wildberries.ru/")
    driver.find_element(By.CSS_SELECTOR, '._close_1b9nk_55').click()
    # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    select_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-card__wrapper'))
    )
    first_element = select_elements[10]
    driver.execute_script('arguments[0].scrollIntoView();', first_element)

def test_upload(driver):
    driver.get("https://www.google.com/?hl=ru")
    icon_photo = driver.find_element(By.CSS_SELECTOR, '.nDcEnd')
    icon_photo.click()
    upload_file = driver.find_element(By.CSS_SELECTOR, '.DV7the')
    upload_file.send_keys(Keys.ENTER)
    upload_file.send_keys("C:/Users/sh4rkkkkkkk/Pictures/Saved Pictures/фон/Honda S2000 (1920x1080).jpg")














