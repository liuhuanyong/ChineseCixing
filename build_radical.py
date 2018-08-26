#!/usr/bin/env python3
# coding: utf-8
# File: build_radic.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-8-26

from urllib import request
from lxml import etree
import chardet

def get_html(url):
    return request.urlopen(url).read().decode('gbk')

def main():
    f = open('radicals.txt', 'w+')
    start = 'http://xh.5156edu.com/bs.html'
    html = get_html(start)
    selector = etree.HTML(html)

    links = ['http://xh.5156edu.com/' + i for i in selector.xpath('//a[@class="fontbox"]/@href')]
    fonts = [i for i in selector.xpath('//a[@class="fontbox"]/text()')]
    font_dict = list(zip(fonts, links))
    for i in font_dict:
        w = i[0]
        link = i[1]
        html = request.urlopen(link).read().decode('GBK', 'ignore')
        selector = etree.HTML(html)
        words = [i for i in selector.xpath('//td/a[@class="fontbox"]/text()')]
        print(link, w, words)
        for wd in words:
            f.write(wd + ':' + w + '\n')
    f.close()




if __name__=='__main__':
    main()