from playwright.sync_api import Page, expect
import re
from time import sleep

# def test_one(page: Page):
#     page.goto("https://www.google.com/")
#     search_field = page.get_by_role('combobox')
#     search_field.fill('anime')
#     search_field.press('Enter')
#     expect(page).to_have_title(re.compile('^anime'))


def test_two(page: Page):
    page.goto("https://www.ivi.ru/")
    page.get_by_text("Назад").click()
    page.locator('[data-test="menu_section_films"]').click()
    sleep(3)


# def test_label(page: Page):
#     page.goto("https://www.ivi.ru/?ivi_search")
#     page.get_by_placeholder('Фильмы, сериалы, жанры и персоны').fill('fkjgfhkd')

def test_by_title(page: Page):
    page.goto("https://www.google.com/")
    field = page.get_by_title('Поиск')
    field.press_sequentially('cat',delay=100)
    sleep(1)
    field.press('Control+a')
    field.press('Backspace')
    sleep(3)

def test_xpath(page: Page):
    page.goto("https://www.ivi.ru/")
    page.get_by_text("Назад").click()
    page.locator('//a[@data-test="menu_section_films"]').click()
    sleep(3)


