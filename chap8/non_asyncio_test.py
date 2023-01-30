import datetime
import requests
from bs4 import BeautifulSoup as bs

url_list = [
    'https://www.google.com/search?q=laptop',
    'https://www.google.com/search?q=mouse',
    'https://www.google.com/search?q=keyboard',
    'https://www.google.com/search?q=monitor',
    'https://www.google.com/search?q=speaker'
]

start_dttm = datetime.datetime.now()
print('Start = {}'.format(start_dttm))

url_request_list = []

for url in url_list:
    rq = requests.get(url)
    html_code = bs(rq.content,"html.parser")

    url_request_list.append(html_code)

end_dttm = datetime.datetime.now()
print('End = {}'.format(end_dttm))
print('Running time = {}'.format(end_dttm - start_dttm))