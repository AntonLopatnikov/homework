import json
from playwright.sync_api import Page, expect, Request, Route, APIResponse
from time import sleep
import re

def test_listen(page: Page):

    def print_request(request: Request):
        print('REQUEST:', request.post_data, request.url)

    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.url, response.status))
    page.goto("https://www.qa-practice.com/")
    page.get_by_role('link', name='Text input').click()
    input_field = page.locator('#id_text_string')
    input_field.fill('Hello')
    input_field.press('Enter')


def test_fetch_response(page: Page):
    page.goto("https://www.ivi.ru/")
    page.locator('.nbl-simpleControlButton__nbl-iconSvg').nth(1).click()
    page.locator('.headerMenu__listItem').nth(1).click()

    with page.expect_response('**/UnreadCount**') as response_event:
        page.locator('.nbl-poster__properties').nth(0).click()

    response = APIResponse(response_event.value)
    expect(response).to_be_ok()
    print(response.url)
    print(response.status)


def test_main_menu(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body[0]['name'] = 'VALERUS BLUNELLI'
        body[0]['url'] = 'https://sun9-69.userapi.com/s/v1/ig2/qQl5z35bNf37fvSgjL_Cv00roJ2hpXBzOBhapRPDsN_yfF3TAcOiHQEquY7qt0RzU-IjNqUAD08e4owuTo4cmeEs.jpg?quality=96&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920&from=bu&cs=1440x0'
        body = json.dumps(body)
        route.fulfill(
            response=response, body=body
        )

    def handle_route2(route: Route):
        url = route.request.url
        url = url.replace('/main-menu-ru-ru-v3.json', '')
        route.continue_(url = url)


    page.route(re.compile('/main-menu-ru-ru-v3.json'), handle_route)
    page.goto("https://www.wildberries.ru/")
    try:
        page.get_by_label('Close').click()
    except:
        pass
    burger = page.get_by_role('button', name='Навигация по сайту')
    burger.click()
    sleep(5)
    menu_link = page.locator('.menu-burger__main-list-link').nth(1)
    expect(menu_link).to_be_visible()
    expect(menu_link).to_be_enabled()
    menu_link.click()
    sleep(5)



def test_samsung(page: Page):

    def change_reg(route: Route):
        url = route.request.url
        print(url)
        url = url.replace('&filter5=15p01', '')
        route.continue_(url = url)

    page.route(re.compile('/product/finder'), change_reg)
    page.goto("https://www.samsung.com/au/smartphones/galaxy-z/")
    price = page.locator('[class="pd21-filter__selector-item-cta"]').nth(4)
    price.is_enabled()
    price.click()
    checkbox = page.locator('[class="checkbox-v3__label-box-icon"]').nth(10)
    checkbox.is_enabled()
    checkbox.click()
    sleep(5)

def test_api(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json(), response.status)
    expect(response).to_be_ok()
    assert response.json()['id'] == 42
    print(type(response))