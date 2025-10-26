import requests

def on_start():
    response = requests.post(
        'https://hh.ru/oauth/token',
        headers ={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    print(response.text)

on_start()


