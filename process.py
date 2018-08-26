#!/usr/bin/env python3
# coding:utf-8
# File:process.py
# Author:lhy<lhy_in_blcu@126.com>
# Date:2018/6/9
from pypinyin import lazy_pinyin
import os

class WordForm:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        charfile = os.path.join(cur_dir, 'chars.txt')
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
        self.stroken_dict = {i.strip().split(':')[0]:[self.char_dict[j.split('/')[0]] for j in i.strip().split(':')[1].split(',')] for i in open(charfile) if i.strip()}

    def get_strokes(self, word):
        strokes = []
        chars = [c for c in word]
        for c in chars:
            stroke = ''.join(self.stroken_dict.get(c, c))
            strokes.append(stroke)
        return strokes

    def get_pinyin(self, word):
        pinyins = lazy_pinyin(word)
        return pinyins


def demo():
    word = '李克强总理今天来我家了,我感到非常荣幸'
    handler = WordForm()
    strokes = handler.get_strokes(word)
    pinyins = handler.get_pinyin(word)

    print(strokes)
    print(pinyins)

if __name__ == '__main__':
    demo()
