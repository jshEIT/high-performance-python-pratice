import random
import string
import urllib.error
import urllib.parse
import urllib.request
from contextlib import closing

import gevent
from gevent import monkey
from gevent.lock import Semaphore

monkey.patch_socket()

def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))

def download(url, semaphore):
    with semaphore:  
        with closing(urllib.request.urlopen(url)) as data:
            return data.read()

def chunked_requests(urls, chunk_size=100):

    semaphore = Semaphore(chunk_size)  
    requests = [gevent.spawn(download, u, semaphore) for u in urls]  
    for response in gevent.iwait(requests):
        yield response

def run_experiment(base_url, num_iter=1000):
    urls = generate_urls(base_url, num_iter)
    response_futures = chunked_requests(urls, 100)  
    response_size = sum(len(r.value) for r in response_futures)
    return response_size

if __name__ == "__main__":
    import time

    delay = 100
    num_iter = 1000
    base_url = f"http://127.0.0.1:8000/add?name=gevent&delay={delay}&"

    start = time.time()
    result = run_experiment(base_url, num_iter)
    end = time.time()
    print(f"Result: {result}, Time: {end - start}")