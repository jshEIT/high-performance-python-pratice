import datetime
import requests
from bs4 import BeautifulSoup as bs
import asyncio

url_list = [
    'https://www.google.com/search?q=laptop',
    'https://www.google.com/search?q=mouse',
    'https://www.google.com/search?q=keyboard',
    'https://www.google.com/search?q=monitor',
    'https://www.google.com/search?q=speaker'
]

start_dttm = datetime.datetime.now()
print('Start = {}'.format(start_dttm))


async def get_html(url):
    rq = await loop.run_in_executor(None, requests.get, url)
    html_code = await loop.run_in_executor(None, bs, rq.content, 'html.parser')

    return html_code

async def main():
    fts = [asyncio.ensure_future(get_html(url)) for url in url_list]
    result = await asyncio.gather(*fts)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


end_dttm = datetime.datetime.now()
print('End = {}'.format(end_dttm))
print('Running time = {}'.format(end_dttm - start_dttm))