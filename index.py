import bs4
import requests

respond = requests.get('https://www.worldometers.info/coronavirus/')

if respond.status_code:
    print('status', respond.status_code)
    web_code = respond.text
    table = web_code.find('<table id="main_table_countries')
    print(table)
else:
    print('error')

