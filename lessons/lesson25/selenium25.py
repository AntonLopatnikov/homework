#https://docs.google.com/presentation/d/1ZtsRzu-RryU1AXMAuOxFuVCyrT_HK8bvibrNWEBbmU8/edit?slide=id.gc6f980f91_0_0#slide=id.gc6f980f91_0_0
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument('start-maximized')
# options.add_argument('--window-size=500,1080')
# options.add_experimental_option('detach', True )
driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.set_window_size(1920, 1080)
driver.get("https://www.google.com/?hl=ru")
print(driver.title)
print(driver.current_url)
search_input =driver.find_element(By.NAME, "q")
search_input.send_keys('cat')
search_click = driver.find_element(By.NAME, "btnK")
search_click.click()
# text_string.submit()
assert "cat" in driver.title








