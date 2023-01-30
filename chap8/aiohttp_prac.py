import asyncio
import random
import string

import aiohttp

def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))

def chunked_http_client(num_chunks):
    """
    URL의 컨텐츠를 가져오는 함수를 반환한다.
    이 함수는 동시에 최대 "new_chunks"만큼만 연결을 연다.
    """
    semaphore = asyncio.Semaphore(num_chunks)  

    async def http_get(url, client_session):  
        nonlocal semaphore
        async with semaphore:
            async with client_session.request("GET", url) as response:
                return await response.content.read()

    return http_get

async def run_experiment(base_url, num_iter=1000):
    urls = generate_urls(base_url, num_iter)
    http_client = chunked_http_client(100)
    responses_sum = 0
    async with aiohttp.ClientSession() as client_session:
        tasks = [http_client(url, client_session) for url in urls]  
        for future in asyncio.as_completed(tasks):  
            data = await future
            responses_sum += len(data)
    return responses_sum

if __name__ == "__main__":
    import time

    loop = asyncio.get_event_loop()
    delay = 100
    num_iter = 1000

    start = time.time()
    result = loop.run_until_complete(
        run_experiment(
            f"http://127.0.0.1:8000/add?name=asyncio&delay={delay}&", num_iter
        )
    )
    end = time.time()
    print(f"Result: {result}, Time: {end - start}")