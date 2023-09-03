# -*- coding: utf-8 -*-
"""
Python 的字符串
"""

# 转义符
print('\n----------- 转义符的使用 -----------')
print('Bob said \"I\'m OK\"')
print('换行符：\n')
print('制表符：\t')
print('斜杠：\\')

# 多行字符串
print('\n----------- 多行字符串 -----------')
multi_row_string = '''Line1
Line2
Line3'''
print(multi_row_string)

# raw 字符串
print('\n----------- raw 字符串: 避免转义符太多 -----------')
print(r'\(~_~)/ \(~_~)/')

print('\n----------- raw 多行字符串: 支持 \' 和 " -----------')
multi_row_string = r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
print(multi_row_string)

"""
字符串格式化
"""
print('\n----------- 字符串 format -----------')
template = 'Life is {}, you need {}'
result = template.format('short', 'Python')
print(result)

print('\n----------- 字符串 format, 指定顺序 -----------')
template = 'Hello {0}, Hello {1}, Hello {2}, Hello {3}.'
result = template.format('World', 'China', 'Beijing', '54pig')
print(result)

print('\n----------- 字符串 format, 指定名称 -----------')
template = 'Hello {w}, Hello {c}, Hello {b}, Hello {p}.'
result = template.format(w='World', c='China', b='Beijing', p='54pig')
print(result)

print('\n----------- 运算符 % 实现字符串拼接 -----------')
name = 'ping'
city = 'ShangHai'
text = 'My name is %s, I work in %s'
print(text % (name, city))
"""
占位符详解
| 符号 | 描述                    |
| :--- | :---------------------- |
| %%   | 用于表示 %              |
| %c   | 格式化字符及其 ASCII 码 |
| %s   | 格式化字符串            |
| %d   | 格式化整数              |
| %f   | 格式化浮点数            |
"""

"""
在 python3 中，默认使用 UTF-8 Unicode 来进行编码，因此我们可以在 python 中输入
任意形式的 Unicode 字符串，都不会遇到像 python2 中遇到的问题
（在 python2 中，需要显式指明该字符串是 Unicode 字符串，文件开始处注释 coding: utf-8）
"""
print('\n----------- 字符串编码问题 -----------')
s = '这是一句中英文混合的 Python 字符串：Hello World!'
print(s)

"""
字符串切片
"""
print('\n----------- 字符串切片 -----------')
s = 'ABCDEFGHIJK'
print(s[0])
print(s[1])
print(s[2])
print(f'第 1 个字符到第 2 个字符：{s[0:2]}')
print(f'第 3 个字符到第 6 个字符：{s[2:6]}')
print(f'第 7 个字符到第 5 个字符：{s[6:3:-1]}')
print(f'指定步长为 2 进行切片取值：{s[0:len(s):2]}')
