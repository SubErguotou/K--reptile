#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 22:44
# @Author  : Eerguotou
# @Site    : 爬取几个网页
# @File    : reptile_img_02.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re
import time
import random

index = 1


def save_jpg(res_url):
    global index
    time.sleep(random.random() * 3)
    r = requests.get(res_url)
    html = BeautifulSoup(r.text, 'html5lib')

    # 解析网站上的图片
    for l in html.find_all('img', {'class': 'j-lazy'}, alt=re.compile("^[0-9]*$")):
        print('正在爬取第%s张图片' % index)
        url02 = l['data-original']
        time.sleep(random.random() * 3)
        html02 = requests.get(url02)
        with open('img/' + str(index) + '.jpg', 'wb') as file:
            file.write(html02.content)
        print('第%s张图片爬取完成' % index)
        index += 1


if __name__ == '__main__':
    url = "https://www.ecysj.net/17585.html"
    # 请求
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html5lib")
    url_list = [url]

    # 解析网站上的内链加入list
    for link in soup.find('div', {'class': 'profile-posts'}).find('ul').find_all('li'):
        if link not in url_list:
            url_list.append(link.find('a')['href'])

    for link in url_list:
        time.sleep(random.random() * 3)
        save_jpg(link)

    print("总共爬了{}张图片".format(index))
