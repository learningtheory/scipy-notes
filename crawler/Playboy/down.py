# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/5/13 上午2:14
"""

from crawler.Playboy import index, root
from crawler.Playboy.index import session, headers

import os
from multiprocessing.pool import ThreadPool

pool = ThreadPool(10)


def mkdir_muti(path):
    folders = []
    while not os.path.isdir(path):
        path, suffix = os.path.split(path)
        folders.append(suffix)
    for folder in folders[::-1]:
        path = os.path.join(path, folder)
        os.mkdir(path)

        # os.mkdir(os.path.join(root, '12'))


if __name__ == '__main__':
    index_url = 'https://www.huainanhai.com/list/index'
    res = session.get(url=index_url, headers=headers, verify='charles-ssl-proxying-certificate.pem')
    mp = index.pb_1(res.text)

    flag = False

    for name, url in mp.items():
        res = session.get(url=url, headers=headers, verify='charles-ssl-proxying-certificate.pem')
        mp_2 = index.pb_2(res.text)
        print(name)
        for name_2, url_2 in mp_2.items():
            res = session.get(url=url_2, headers=headers, verify='charles-ssl-proxying-certificate.pem')
            mp_3 = index.pb_3(res.text)
            print('\t' + name_2)
            for name_3, url_3 in mp_3.items():
                path = root + '/{}/{}'.format(name, name_2)
                mkdir_muti(path)
                res = session.get(url=url_3, headers=headers, verify='charles-ssl-proxying-certificate.pem')
                args = {1: res.text, 2: path + '/' + name_3}
                print('\t' + name_3)
                # if name_3 == '第11节穿衬衣注意的细节':
                #     flag = True
                # if flag:
                pool.map(index.down_mp4, [args])
