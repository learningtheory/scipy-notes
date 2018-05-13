# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/5/13 上午2:06
"""
import requests
from pyquery import PyQuery as pq

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
    'cookie': 'PHPSESSID=f2esdv3aeq496rjojvbq1it7s0; gr_user_id=dc1cf290-261d-49cc-a6da-f8cba4fb2073; gr_session_id_82183079f08abc9a=6af0f704-280e-4c26-ab60-f1da369f073a_true; Hm_lvt_23e09f6e96daf10d88b29c0bbecbeac5=1526140808,1526141129,1526141844; session_id=152614186651ff97a95873959cd06581; login_user_id=3519738; c5ac325b7aebabcd02405df9f73f5592=17600699137; d49b5cd9a853fefd7e35da07174b7b2b=76c166aea22aa111f5d2bf0891cc77b1; Hm_lvt_54894565beb134236e57c661d1fa2a2e=1526141959; unfold=1; Hm_lpvt_54894565beb134236e57c661d1fa2a2e=1526142399; Hm_lpvt_23e09f6e96daf10d88b29c0bbecbeac5=1526142490',
}

session = requests.Session()


def pb_1(content):
    """
    {'网聊大师': 'https://www.huainanhai.com/list/index/23', '微信聊天攻略': 'https://www.huainanhai.com/list/index/44', '校园恋爱': 'https://www.huainanhai.com/list/index/26', '相亲攻略': 'https://www.huainanhai.com/list/index/25', '搭讪技巧': 'https://www.huainanhai.com/list/index/28', '型男计划': 'https://www.huainanhai.com/list/index/22', '约会课程': 'https://www.huainanhai.com/list/index/29'}
    :param content:
    :return:
    """
    a = pq(content)
    ms = a('body > div.container.bg-gray > div.banner > div.wrap.sub-nav > ul > li')
    mp = {}
    for i in ms.items():
        h3 = i('a')
        url = 'https://www.huainanhai.com{}'.format(h3('a').attr('href'))
        name = h3.text()
        mp[name] = url
    return mp


def pb_2(content):
    """
    {'处理信息': 'https://www.huainanhai.com/course/detail/64', '聊天案例': 'https://www.huainanhai.com/course/detail/63', '社交软件技巧进阶': 'https://www.huainanhai.com/course/detail/62', '社交软件': 'https://www.huainanhai.com/course/detail/61', '微信聊天': 'https://www.huainanhai.com/course/detail/55', '微信聊天案例': 'https://www.huainanhai.com/course/detail/56', '婚恋网': 'https://www.huainanhai.com/course/detail/57', '社交案例': 'https://www.huainanhai.com/course/detail/58', '微信聊天技巧': 'https://www.huainanhai.com/course/detail/60'}
    :param content:
    :return:
    """
    a = pq(content)

    ms = a('.moda-list')('ul')('li')

    mp = {}

    for i in ms.items():
        h3 = i('h3')
        url = 'https://www.huainanhai.com{}'.format(h3('a').attr('href'))
        name = h3.text()
        mp[name] = url
    return mp


def pb_3(content):
    """
    {'第1节避免信息产生误会免费': 'https://www.huainanhai.com/course/play/667', '第2节不回信息怎么处理': 'https://www.huainanhai.com/course/play/668', '第3节短信互动的基本原则': 'https://www.huainanhai.com/course/play/669', '第4节快速了解微信朋友圈建设': 'https://www.huainanhai.com/course/play/670', '第5节手机必备的几款社交约会应用': 'https://www.huainanhai.com/course/play/671', '第6节为什么女人在社交软件中不理你': 'https://www.huainanhai.com/course/play/672', '第7节邀约前的铺垫': 'https://www.huainanhai.com/course/play/673', '第8节怎么通过短信快速邀约': 'https://www.huainanhai.com/course/play/674'}

    :param content:
    :return:
    """
    a = pq(content)

    ms = a('body > div.container > div.wrap > div.content > div > div.bd.chapters > a')

    mp = {}

    for i in ms.items():
        url = 'https://www.huainanhai.com{}'.format(i.attr('href'))
        name = i.text()
        mp[name] = url
    return mp


def down_mp4(args):
    c = args.get(1)
    path = args.get(2)
    import base64
    a = c.find('base64decode(')
    b = a + c[a:].find(');')
    url = base64.b64decode(c[a + 14: b - 2]).decode('utf-8')
    print("{}".format(url))
    # with open('{}.mp4'.format(path), 'wb') as file:
        # print(url)
        # file.write(session.get(url=url, headers=headers, verify='charles-ssl-proxying-certificate.pem').content)
