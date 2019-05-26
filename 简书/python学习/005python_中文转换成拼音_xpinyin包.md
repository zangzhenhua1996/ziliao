```
# coding:utf-8
from xpinyin import Pinyin
p = Pinyin()

# 默认以'-'为分割符
a = p.get_pinyin(u"上海")
print(a)

# 默认以'-'分割,显示音调
b = p.get_pinyin(u'上海', show_tone_marks=True)
print(b)

# 删除分割符
c = p.get_pinyin(u'上海', '')
print(c)

# 设置空白格为分割符
d = p.get_pinyin(u'上海', ' ')
print(d)

d1 = p.get_initial(u'上')
print(d1)

d2 = p.get_initials(u'上海')
print(d2)

d3 = p.get_initials(u'上海', u'')
print(d3)

d4 = p.get_initials(u'上海', u' ')
print(d4)


# 如果方法中传入变量，那么直接加前缀是不可以了，而是要将变量转为utf-8编码：
wordvalue = '中国'
wv = unicode(wordvalue, 'utf-8')
s = p.get_initials(wv, u'').lower()
print(s)
```
