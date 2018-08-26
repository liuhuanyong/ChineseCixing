#!/usr/bin/env python3
# coding:utf-8
# File:cixing.py
# Author:lhy<lhy_in_blcu@126.com>
# Date:2018/6/9
from pypinyin import lazy_pinyin
import os

class ChineseCixing:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        strokefile = os.path.join(cur_dir, 'strokes.txt')
        radicalfile = os.path.join(cur_dir, 'radicals.txt')
        self.char_dict = {
            "点": "㇔",
            "横": "㇐",
            "横钩": "㇖",
            "横撇": "㇇",
            "横撇弯钩": "㇌",
            "横斜钩": "⺄",
            "横折": "㇕",
            "横折竖钩": "㇆",
            "横折提": "㇊",
            "横折弯": "㇍",
            "横折弯钩": "㇈",
            "横折折": "㇅",
            "横折折撇": "㇋",
            "横折折折": "㇎",
            "横折折折钩": "㇡",
            "捺": "㇏",
            "撇": "㇓",
            "撇点": "㇛",
            "撇折": "㇜",
            "竖": "㇑",
            "竖钩": "㇚",
            "竖提": "㇙",
            "竖弯": "㇄",
            "竖弯横钩": "㇟",
            "竖折": "㇗",
            "竖折撇": "ㄣ",
            "竖折折": "㇞",
            "竖折折钩": "㇉",
            "提": "㇀",
            "弯钩": "㇁",
            "卧钩": "㇃",
            "斜钩": "㇂",
            }
        self.stroke_dict = {i.strip().split(':')[0]:[self.char_dict[j.split('/')[0]] for j in i.strip().split(':')[1].split(',')] for i in open(strokefile) if i.strip()}
        self.radical_dict = {i.strip().split(':')[0]:i.strip().split(':')[1] for i in open(radicalfile) if i.strip()}

    '''获取汉字笔画'''
    def get_strokes(self, word):
        strokes = []
        chars = [c for c in word]
        for c in chars:
            stroke = ''.join(self.stroke_dict.get(c, c))
            strokes.append(stroke)
        return strokes

    '''获取汉字汉语拼音'''
    def get_pinyin(self, word):
        pinyins = lazy_pinyin(word)
        return pinyins

    '''获取汉字偏旁部首'''
    def get_radical(self, word):
        radicals = []
        chars = [c for c in word]
        for c in chars:
            stroke = self.radical_dict.get(c, c)
            radicals.append(stroke)
        return radicals


def demo():
    word = '自然语言处理是皇冠上的一颗明珠'
    handler = ChineseCixing()
    strokes = handler.get_strokes(word)
    pinyins = handler.get_pinyin(word)
    radicals = handler.get_radical(word)

    print('strokes', strokes)
    print('pinyins', pinyins)
    print('radicals', radicals)

if __name__ == '__main__':
    demo()
