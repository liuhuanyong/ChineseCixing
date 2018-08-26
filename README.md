# WordFormSearch
WordFormSearch,针对中文词语的笔画拆解，偏旁查询，拼音转换接口．在当前的中文信息处理当中，语言外部形式上的特征在各个任务中扮演着越来越重要的角色，本项目目的是为提供这一接口


# 使用方式

        word = '汉字与拼音的转换'
        handler = WordForm()
        strokes = handler.get_strokes(word)
        pinyins = handler.get_pinyin(word)

        print(strokes)
        print(pinyins)

# 测试样例
        content = '李克强总理今天来我家了,我感到非常荣幸'
        strokes: ['㇐㇑㇓㇏㇇㇚㇐', '㇐㇑㇑㇕㇐㇓㇟', '㇕㇐㇉㇑㇕㇐㇑㇕㇐㇑㇐㇔', '㇔㇓㇑㇕㇐㇔㇂㇔㇔', '㇐㇐㇑㇀㇑㇕㇐㇐㇑㇐㇐', '㇓㇏㇔㇇', '㇐㇐㇓㇏', '㇐㇔㇓㇐㇑㇓㇏', '㇓㇐㇚㇀㇂㇓㇔', '㇔㇔㇇㇐㇓㇁㇓㇓㇓㇏', '㇇㇚', ',', '㇓㇐㇚㇀㇂㇓㇔', '㇐㇓㇐㇑㇕㇐㇂㇓㇔㇔㇂㇔㇔', '㇐㇜㇔㇐㇑㇀㇑㇚', '㇑㇐㇐㇐㇑㇐㇐㇐', '㇑㇔㇓㇔㇇㇑㇕㇐㇑㇆㇑', '㇐㇑㇑㇔㇇㇐㇑㇓㇏', '㇐㇑㇐㇔㇓㇐㇐㇑']
        pinying:['li', 'ke', 'qiang', 'zong', 'li', 'jin', 'tian', 'lai', 'wo', 'jia', 'le', ',', 'wo', 'gan', 'dao', 'fei', 'chang', 'rong', 'xing']


