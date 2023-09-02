"""
【字典】
查找速度快，无论是 10 个元素还是 10 万个元素，查找速度都一样
key 必须使用不可变类型，如果使用可变类型（比如：list）会报错
缺点：内存占用大
"""

print('\n----------- 字典演示 -----------')
d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49,
    'Gaven': 86
}
print(d)

print('\n----------- 从字典中获取元素 - dict[key] -----------')
print('Alice 的成绩：', d['Alice'])
try:
    print(d['pig'])
except KeyError as e:
    print('key 不存在，', repr(e))

print('\n----------- 从字典中获取元素（避免 KeyError） - dict.get(key) -----------')
print(d.get('pig'))

print('\n----------- 字典的更新操作：已存在就更新，不存在就添加 -----------')
d['Alice'] = 69
d['ppp'] = 99
print(d)

print('\n----------- 字典的删除操作：pop() / pop(key) -----------')
print(fr'''
删除 ['ppp'], pop() 方法会返回被删除元素的 value：{d.pop('ppp')}
''')

print('\n----------- 判断 key 是否存在于字典中 -----------')
if 'ppp' in d.keys():
    print(d['ppp'])
else:
    print('{} not in tuple'.format('ppp'))

print('\n----------- 遍历字典 -----------')
# for 循环遍历字典的所有 key
for key in d.keys():
    print(key)
# for 循环遍历字典的所有 value
for value in d.values():
    print(value)
# for 循环遍历字典的所有 key，并找出 value 大于 60 的
for key in d:
    value = d[key]
    if value > 60:
        print(key, value)
# for 循环遍历字典的所有 key，并找出 value 大于 60 的
for key, value in d.items():
    if value > 60:
        print(key, value)

print('\n----------- 字典的长度 -----------')
print(len(d))
print(len(d.keys()))
print(len(d.values()))

print('\n----------- 清空 -  clear() -----------')
d.clear()
print(d)

print('\n----------- 示例 - 使用字典存放 3 个同学的多次成绩 -----------')
d = dict()
# 用 list 来存放每位同学的成绩
d['Alice'] = []
d['Bob'] = []
d['Candy'] = []
# 开始填充成绩
d['Alice'].append(50)
d['Alice'].append(61)
d['Alice'].append(66)
d['Bob'].append(80)
d['Bob'].append(61)
d['Bob'].append(66)
d['Candy'].append(88)
d['Candy'].append(75)
d['Candy'].append(90)
# 输出打印每个同学的成绩
for key, value in d.items():
    for index, score in enumerate(value, 1):
        print('{} 第 {} 次成绩：{}'.format(key, index, score))
