# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/10 下午5:38
"""
from multiprocessing.pool import ThreadPool

pool = ThreadPool(9)

import requests

session = requests.session()

headers = {
    "user-agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'
}


def request_url(url):
    res = session.get(url=url, headers=headers)

    print(res.status_code)

    if res.status_code != 200:
        print(res.reason)
    print(len(res.text))
    # print(res.content)


if __name__ == "__main__":

    urls = []

    for i in range(100):
        urls.append('https://blog.csdn.net/qq_29719097/article/details/79728478')

    pool.map(request_url, urls)
