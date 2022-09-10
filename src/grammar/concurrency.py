import concurrent.futures
import requests
import asyncio
import aiohttp


def download_one(url):
    return url
    # res = requests.get(url)
    # print('Read {} from {}'.format(len(res.content), url))


class ConcurrentFutures(object):

    def download_all(self, sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            to_do = []
            for site in sites:
                future = executor.submit(download_one, site)
                to_do.append(future)

            results = []
            for future in concurrent.futures.as_completed(to_do):
                res = future.result()
                results.append(res)
            print(results)


async def download_one_a(url):
    async with aiohttp.ClientSession() as session:
        print(url)
        # async with session.get(url) as resp:
        #     print('Read {} from {}'.format(resp.content, url))


class ConcurrentAsyncio(object):
    async def download_all(self, sites):
        tasks = [asyncio.create_task(download_one_a(site)) for site in sites]
        await asyncio.gather(*tasks)
