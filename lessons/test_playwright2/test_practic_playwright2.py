from playwright.sync_api import Page, expect, BrowserContext, Dialog
from time import sleep

from selenium.common import NoSuchElementException


# def test_text_visible(page:Page):
#     page.goto('https://www.ivi.ru/movies')
#     regs = page.locator('.filterDropdown__input-text').filter(has_text='Артхаус')
#     expect(regs).not_to_be_visible()
#     page.locator('.filtersDesktop__plank').filter(has_text='Жанры').first().click()
#     expect(regs).to_be_visible()

def test_two(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/disabled")
    button = page.locator('#submit-id-submit')
    expect(button).to_be_disabled()
    page.locator('#id_select_state').select_option('Enabled')
    expect(button).to_be_enabled()
    expect(button).to_have_text('Submit')
    expect(button).to_contain_text('ubm')


def test_value(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_field = page.locator('#id_text_string')
    input_field.fill('hgkjhj')
    expect(input_field).to_have_value('qwert')


def test_sort(page: Page):
    page.goto("https://www.wildberries.ru/catalog/obuv/muzhskaya/kedy-i-krossovki?sort=popular&page=1&cardsize=c516x688")
    sleep(3)
    check_text = page.get_by_text('Мужские кеды и кроссовки')
    expect(check_text).to_be_visible()
    expect(check_text).to_have_text('Мужские кеды и кроссовки')
    sneakers = page.locator('.product-card__link').locator('nth=0')
    expect(sneakers).to_be_visible()
    href = sneakers.get_attribute('href')
    print(f'первые кроссовки: {href}')
    page.get_by_text('По популярности').click()
    page.get_by_text('По возрастанию цены').click()
    expect(page.get_by_text('По возрастанию цены')).to_have_text('По возрастанию цены')
    page.wait_for_timeout(5000)
    sneakers2 = page.locator('.product-card__link').locator('nth=0')
    expect(sneakers2).to_be_visible()
    href2 = sneakers2.get_attribute('href')
    print(f'вторые кроссовки: {href2}')


def test_tabs(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/link")
    link = page.locator('#new-page-link')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    page.get_by_role('link', name = 'New tab button').click()


def test_hover(page: Page):
    page.goto("https://www.wildberries.ru/")
    try:
        page.get_by_label('Close').click()
    except:
        pass
    burger = page.get_by_role('button', name = 'Навигация по сайту')
    burger.click()
    shoes = page.locator('.menu-burger__main-list-item').nth(13)
    shoes.hover()
    men_shoes = page.locator('body > div.wrapper.j-wrapper > '
            'div.menu-burger.j-menu-burger.menu-burger--active > '
            'div.menu-burger__drop.j-menu-burger-drop.menu-burger__drop--custom.menu-burger__drop--active.j-menu-active > '
            'div > div.menu-burger__drop-list-item.j-menu-drop-item.j-menu-drop-item-629.menu-burger__drop-list-item--active > '
            'div > div.menu-burger__first.j-menu-inner-column > ul > li:nth-child(4) > span'
    )
    if men_shoes.is_enabled():
        print(' раздел найден')
    else:
        print(' раздел не найден')
    men_shoes.click()
    sneakers = page.get_by_text('Кеды и кроссовки')
    sneakers.click()
    check_text = page.get_by_text('Мужские кеды и кроссовки')
    expect(check_text).to_be_visible()
    try:
        expect(check_text).to_have_text('Мужские кеды и кроссовки')
        print(' проверка пройдена')
    except:
        print('проверка не пройдена')



def test_drag_and_drop(page: Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    drag_me = page.locator('#rect-draggable')
    drag_here = page.locator('#rect-droppable')
    drag_me.drag_to(drag_here)
    check_text = page.locator('#rect-droppable')
    try:
        expect(check_text).to_be_visible()
        print(f' Проверка пройдена: {check_text.inner_text()}')
    except:
        print(' Проверка не пройдена')


def test_allert(page: Page):

    def cansel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.dismiss()

    def fill_accept(alert: Dialog):
        alert.accept('some test')

    # page.on('dialog', fill_accept)
    page.on('dialog', lambda alert: alert.accept('another text'))
    page.goto("https://www.qa-practice.com/elements/alert/prompt")
    page.get_by_role('link', name = 'Click').click()
    sleep(3)




