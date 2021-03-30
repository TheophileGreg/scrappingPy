token = 'https://www.leboncoin.fr/recherche?locations=Nîmes_30000__43.83512_4.35856_10000'

import requests
# for i in pages:
#     response = requests.get(i)

import itertools as it
import pandas as pd

import random
import time
# !pip install fake-useragent
from fake_useragent import UserAgent

ua = UserAgent()
time.sleep(random.randrange(1, 5))

proxies = pd.read_csv('proxy_list.txt', header=None)
proxies = proxies.values.tolist()
proxies = list(it.chain.from_iterable(proxies))
proxy_pool = it.cycle(proxies)
proxy = next(proxy_pool)
response = requests.get(token,
                        proxies={
                            "http": proxy,
                            "https": proxy
                        },
                        headers={'User-Agent': ua.random},
                        timeout=5)
print(response)

from urllib.request import urlopen
with urlopen("https://www.seloger.com/robots.txt") as stream:
    print(stream.read().decode("utf-8"))

# from urllib.request import urlopen
# with urlopen("https://www.leboncoin.fr/") as stream:
#     print(stream.read().decode("utf-8"))
# requests.utils.default_user_agent()
