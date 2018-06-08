#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import re
import sqlite3
import time

import requests
from lxml import etree
from requests.exceptions import RequestException

count = 1  # 爬取页码
count_sleep = 0.5  # 爬取延时
url_imdex = "http://www.shuaia.net/"
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"}


def getPages(urls):
    """获取页面信息"""
    print('开始获取页面信息! url=', urls)
    try:
        res = requests.get(urls, headers=headers)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            return res.text
        else:
            return None
    except RequestException:
        print('获取页面信息异常! url=', urls)
        return None


def parseClass(context):
    """解析分类"""
    html = etree.HTML(context)
    items = html.xpath('//div[@class="nav_nav"]')[0]
    for item in items:
        yield{
            'class': item.xpath('a/text()')[0].split()[0],  # 分类名
            'url': item.xpath('a/@href')[0]  # 分类URL
        }


def parseTag(context):
    """解析标签"""
    html = etree.HTML(context)
    items = html.xpath('//div[@id="hot-tags"]/div/div/ul/li')
    for item in items:
        yield{
            'tag': item.xpath('a/text()')[0],  # 标签名
            'url': 'http://www.shuaia.net' + item.xpath('a/@href')[0]  # 标签URL
        }


def parseClassPages(context):
    """解析分类页面"""

    def parse_context(url):
        return getPages(url)

    index = 1
    while index <= count:
        try:
            if index == 1:
                html = parse_context(context['url'])
            else:
                html = parse_context(context['url'] + 'index_{}.html'.format(index))
            pages = etree.HTML(html)
            items = pages.xpath('//a[@class="item-img"]')
            for item in items:
                yield{
                    'class': context['class'],  # 分类名
                    'tag': None,  # 标签名
                    'img': item.xpath('img/@src')[0],  # 主图地址
                    'url': item.xpath('@href')[0]  # 小哥哥URL
                }
        except Exception:
            pass
        index += 1


def parseTagPages(context):
    """解析标签页面"""
    def parse_context(url):
        return getPages(url)

    index = 1
    while index <= count:
        try:
            html = getPages(context['url'] + '&page={}'.format(index-1))
            pages = etree.HTML(html)
            items = pages.xpath('//a[@class="item-img"]')
            for item in items:
                yield{
                    'class': None,  # 分类名
                    'tag': context['tag'],  # 标签名
                    'img': item.xpath('img/@src')[0],  # 主图地址
                    'url': item.xpath('@href')[0]  # 小哥哥URL
                }
        except Exception:
            pass
        index += 1


def parsePages(context):
    """解析小哥哥页面"""
    try:
        html = etree.HTML(context)
    except Exception:
        return None

    items = html.xpath('//div[@class="wr-single-right"]')

    def imgs(context):
        img_count = 1
        while img_count:
            if img_count == 1:
                img_html = getPages(context)
            else:
                img_html = getPages(context.replace('.html', '_' + str(img_count) + '.html'))
            if img_html is None:
                break
            imghtml = etree.HTML(img_html)
            imghtml = imghtml.xpath('//div[@class="wr-single-content-list"]/p/a/img/@src')
            for i in imghtml:
                yield 'http://www.shuaia.net' + i
            img_count += 1

    for item in items:
        yield{
            'title': item.xpath('//div[@class="wr-sigle-intro"]/h1/text()')[0],  # 标题
            'img': imgs(item.xpath('//div[@id="bdshare"]/@data')[0].split("','")[0][8:])  # 图片地址
        }


# 连接数据库
conn = sqlite3.connect('data.db')
# 获取页面信息
page_html = getPages(url_imdex)
# 解析分类信息去重储存到数据库
for i in parseClass(page_html):
    print('开始读取 {} 信息!'.format(i['class']))
    for ii in parseClassPages(i):
        cursor = conn.cursor()
        cursor.execute('select id from data where url=?', (ii['url'],))
        values = cursor.fetchall()
        cursor.close()
        if values:
            cursor = conn.cursor()
            cursor.execute('update data set class = ? where id = ?', (ii['class'], values[0][0]))
            conn.commit()
            cursor.close()
        else:
            cursor = conn.cursor()
            cursor.execute('insert into data (class, url, img) values (?, ?, ?)', (ii['class'], ii['url'], ii['img'],))
            conn.commit()
            cursor.close()
    time.sleep(count_sleep)
# 解析标签信息去重储存到数据库
for i in parseTag(page_html):
    print('开始读取 {} 信息!'.format(i['tag']))
    for ii in parseTagPages(i):
        cursor = conn.cursor()
        cursor.execute('select id from data where url=?', (ii['url'],))
        values = cursor.fetchall()
        cursor.close()
        if values:
            cursor = conn.cursor()
            cursor.execute('update data set tag = ? where id = ?', (ii['tag'], values[0][0]))
            conn.commit()
            cursor.close()
        else:
            cursor = conn.cursor()
            cursor.execute('insert into data (tag, url, img) values (?, ?, ?)', (ii['tag'], ii['url'], ii['img'],))
            conn.commit()
            cursor.close()
    time.sleep(count_sleep)

# 清空image表
cursor_del = conn.cursor()
cursor_del.execute("DELETE from image;")
conn.commit()
cursor_del.close

# 抓取保存小哥哥图片信息
cursor = conn.cursor()
cursor_re = conn.cursor()
cursor_img = conn.cursor()
cursor.execute('select id, url from data')
for url_s in cursor:
    page_html = getPages(url_s[1])
    for page in parsePages(page_html):
        cursor_re.execute('update data set title = ? where id = ?', (page['title'], url_s[0]))
        im = 0
        for img_url in page['img']:
            cursor_img.execute('insert into image (PID, img, title) values (?, ?, ?)', (url_s[0], img_url, page['title'] + "_" + str(im),))

            # 储存图片
            try:
                if not os.path.exists(page['title']):
                    os.makedirs(page['title'])
                print('图片开始保存!: {}'.format(page['title'] + "_" + str(im) + ".jpg"))
                path = os.path.join("./", page['title'])
                save_pic = path + "/" + page['title'] + "_" + str(im) + ".jpg"
                saveImg = requests.get(img_url, headers=headers).content
                with open(save_pic, 'wb') as f:
                    f.write(saveImg)
                time.sleep(count_sleep)
            except Exception:
                print('图片保存失败!: {}'.format(page['title'] + "_" + str(im) + ".jpg"))

            im += 1
        conn.commit()
cursor.close()
cursor_re.close()
cursor_img.close()

# 关闭数据库
conn.close()
