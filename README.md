# ChineseCixing
ChineseCixing,针对中文词语的笔画拆解，偏旁查询，拼音转换接口．在当前的中文信息处理当中，语言外部形式上的特征在各个任务中扮演着越来越重要的角色，本项目目的是为提供这一接口


# 使用方式
    from cixing import *
    handler = ChineseCixing()
    strokes = handler.get_strokes(s)
    pinyins = handler.get_pinyin(s)
    radicals = handler.get_radical(s)

# 测试样例
    s = '自然语言处理是皇冠上的一颗明珠'
    handler = ChineseCixing()
    strokes = handler.get_strokes(s)
    pinyins = handler.get_pinyin(s)
    radicals = handler.get_radical(s)

    print('strokes', strokes)
    print('pinyins', pinyins)
    print('radicals', radicals)

    strokes: [
          '㇓㇑㇕㇐㇐㇐',
          '㇓㇇㇔㇔㇐㇓㇏㇔㇔㇔㇔㇔',
          '㇔㇊㇐㇑㇕㇐㇑㇕㇐',
          '㇔㇐㇐㇐㇑㇕㇐',
          '㇓㇇㇏㇑㇔',
          '㇐㇐㇑㇀㇑㇕㇐㇐㇑㇐㇐',
          '㇑㇕㇐㇐㇐㇑㇐㇓㇏',
          '㇓㇑㇕㇐㇐㇐㇐㇑㇐',
          '㇔㇇㇐㇐㇓㇟㇐㇚㇔',
          '㇑㇐㇐',
          '㇓㇑㇕㇐㇐㇓㇆㇔',
          '㇐',
          '㇑㇕㇐㇐㇐㇑㇓㇔㇐㇓㇑㇕㇓㇔',
          '㇑㇕㇐㇐㇓㇆㇐㇐',
          '㇐㇐㇑㇀㇓㇐㇐㇑㇓㇏'
          ]

    pinyins: ['zi', 'ran', 'yu', 'yan', 'chu', 'li', 'shi', 'huang',
                'guan', 'shang', 'de', 'yi', 'ke', 'ming', 'zhu']
    radicals: ['自', '灬', '讠', '言', '夂', '王', '日', '白',
                '冖', '一', '白', '一', '页', '日', '王']



