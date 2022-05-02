# -*- coding:UTF-8 -*-
"""
作者:尘封
日期:2022年04月09日
"""

# 英文词频统计
# def getText():
#     txt = open("hamlet.txt","r").read()
#     txt = txt.lower()
#     for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':
#         txt = txt.replace(ch," ")    # 将文本中特殊字符替换为空格
#     return txt
# hamletTxt = getText()
# words = hamletTxt.split()
# counts = {}
# for word in words:
#     counts[words] = counts.get(word,0) + 1
# items = list(counts.items())
# items.sort(key = lambda x:x[1],reverse=True)
# for i in range(10):
#     word,count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))


# 构建排除词汇库排除出现的无关文章大意的介词，冠词等，猜出文章大意
# excludes = {"the","and","of","you","a","i","my","in"}  # 可以继续添加排除更多的无关词
# def getText():
#     txt = open("hamlet.txt","r").read()
#     txt = txt.lower()
#     for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':
#         txt = txt.replace(ch," ")    # 将文本中特殊字符替换为空格
#     return txt
# hamletTxt = getText()
# words = hamletTxt.split()
# counts = {}
# for word in words:
#     counts[words] = counts.get(word,0) + 1
# for word in excludes:
#     del(counts[word])
# items = list(counts.items())
# items.sort(key = lambda x:x[1],reverse=True)
# for i in range(10):
#     word,count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))


# 《三国演义》人物出场统计
import jieba
txt = open("三国演义.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:      # 排除单个字符的分词结果
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

# 修改后
import jieba
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
txt = open("三国演义.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == '诸葛亮' or word == '孔明曰':
        rword = '孔明'
    elif word == '关公' or word == '云长':
        rword = '关羽'
    elif word == '玄德' or word == '丞相':
        rword = '曹操'
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(5):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))